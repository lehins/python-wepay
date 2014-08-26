import json, warnings
from six.moves import urllib
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

from wepay.exceptions import *

class Post(object):
    """This is a helper class that uses either `urllib` or `requests` library to
    perform POST requests.

    """
    
    def __init__(self, use_requests=None, silent=None):
        self._use_requests = HAS_REQUESTS and (
            use_requests is None or use_requests)
        if not silent and use_requests and not self._use_requests:
            message = "Using requests library was specified, but there was a problem " \
                      "importing it. Falling back to urllib."
            if silent is not None:
                raise WePayWarning(message)
            warnings.warn(message, WePayWarning)


    def __call__(self, url, params, headers, timeout):
        if self._use_requests:
            return self._post_requests(url, params, headers, timeout)
        return self._post_urllib(url, params, headers, timeout)


    def _post_urllib(self, url, params, headers, timeout):
        data = urllib.parse.urlencode(params).encode('utf-8')
        request = urllib.request.Request(url, data=data, headers=headers)
        try:
            response = urllib.request.urlopen(request, timeout=timeout)
        except urllib.error.HTTPError as exc:
            try:
                kwargs = json.loads(exc.read().decode('utf-8'))
            except ValueError:
                kwargs = {}
            self._raise_error(exc, exc.code, **kwargs)
        except urllib.error.URLError as exc:
            raise WePayConnectionError(exc)
        return json.loads(response.read().decode('utf-8'))


    def _post_requests(self, url, params, headers, timeout):
        data = json.dumps(params)
        try:
            response = requests.post(
                url, data=data, headers=headers, timeout=timeout)
            response.raise_for_status()
        except requests.exceptions.HTTPError as exc:
            try:
                kwargs = exc.response.json()
            except ValueError: # JSONDecodeError is a subclass of ValueError
                kwargs = {}
            self._raise_error(exc, exc.response.status_code, **kwargs)
        except requests.exceptions.RequestException as exc:
            raise WePayConnectionError(exc)
        return response.json()


    def _raise_error(self, exc, status_code, **kwargs):
        if status_code >= 500:
            raise WePayServerError(exc, status_code, **kwargs)
        if status_code >= 400:
            raise WePayClientError(exc, status_code, **kwargs)



class cached_property(object):

    def __init__(self, fget):
        self.fget = fget
        self.__doc__ = fget.__doc__
        self.__name__ = fget.__name__
        self.__module__ = fget.__module__
        self._key = "_%s" % fget.__name__


    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = getattr(obj, self._key, None)
        if value is None:
            value = self.fget(obj)
            setattr(obj, self._key, value)
        return value


    def __set__(self, obj, value):
        setattr(obj, self._key, value)
