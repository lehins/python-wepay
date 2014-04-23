import json, warnings
from six.moves import urllib
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

from wepay.exceptions import WePayWarning, WePayError, WePayConnectionError

class Post(object):
    
    def __init__(self, timeout=None, use_requests=None, silent=None):
        self._use_requests = HAS_REQUESTS and (
            True if use_requests is None else use_requests)
        if not silent and use_requests and not self._use_requests:
            message = "Using requests library was specified, but there was a problem " \
                      "importing it. Falling back to urllib."
            if silent is not None:
                raise WePayWarning(message)
            warnings.warn(message, WePayWarning)
        self._timeout = timeout


    def __call__(self, url, params, headers):
        params = params or {}
        if self._use_requests:
            data = json.dumps(params)
            return self._post_requests(url, data, headers)
        return self._post_urllib(url, params, headers)


    def _post_urllib(self, url, data, headers):
        data = urllib.parse.urlencode(data).encode('utf-8')
        request = urllib.request.Request(url, data=data, headers=headers)
        try:
            response = urllib.request.urlopen(request, timeout=self._timeout)
            return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            response = json.loads(e.read().decode('utf-8'))
            raise WePayError(response['error'], response['error_description'], 
                             response['error_code'])
        except urllib.error.URLError as e:
            raise WePayConnectionError(e, str(e))


    def _post_requests(self, url, data, headers):
        try:
            response = requests.post(
                url, data=data, headers=headers, timeout=self._timeout)
        except requests.exceptions.RequestException as e:
            raise WePayConnectionError(e, str(e))
        response_json = response.json()
        if 400 <= response.status_code <= 599:
            raise WePayError(
                response_json['error'], response_json['error_description'],
                response_json['error_code'])
        return response_json