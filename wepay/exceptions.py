import warnings

__all__ = [
    'WePayWarning', 'WePayError', 'WePayClientError', 'WePayServerError', 
    'WePayConnectionError'
]



class WePayWarning(UserWarning):
    pass
    


class WePayError(Exception):
    """Raised in case API call was not successfull.  `WePay API Errors Documentation
    <https://www.wepay.com/developer/reference/errors>`_

    """
    def __init__(self, http_error, status_code, 
                 error=None, error_description=None, error_code=None):
        self._http_error = http_error
        self._status_code = status_code
        self._error = error
        self._error_code = error_code or -1
        self._error_description = error_description or ""


    def __str__(self):
        return "HTTP %s - %s (%s): %s" % (
            self.status_code, self.error, self.error_code, self.error_description)


    @property
    def status_code(self):
        """Error Code a specified by RFC 2616."""
        return self._status_code


    @property
    def http_error(self):
        """Instance of :exc:`urllib.error.HTTPError` or
        :exc:`requests.exceptions.HTTPError`, depending on the library you chose.

        """
        return self._http_error


    @property
    def error(self):
        """``error`` - parameter return from WePay: `possible values
        <https://www.wepay.com/developer/reference/errors>`_
        
        """
        return self._error


    @property
    def error_code(self):
        """``error_code`` - parameter return from WePay: `possible values
        <https://www.wepay.com/developer/reference/errors>`_
        
        """
        return self._error_code


    @property
    def error_description(self):
        """A human readable ``error_description`` that explains why the error happened.
        `possible values <https://www.wepay.com/developer/reference/errors>`_
        """
        return self._error_description


    @property
    def code(self):
        warnings.warn("'code' is deprecated in favor of 'error_code'",
                      DeprecationWarning)
        return self.error_code


    @property
    def message(self):
        warnings.warn("'message' is deprecated in favor of 'error_description'",
                      DeprecationWarning)
        return self.error_description




class WePayClientError(WePayError):
    """This is a 4xx type error, which, most of the time, carries important
    information about the object of interest.

    """



class WePayServerError(WePayError):
    """This is a 5xx type error, which, most of the time, means there is an
    error in implemetation or some unknown WePay Error, in latter case there is
    a chance there will be no `error`, `error_code` or `error_description` from
    WePay. It is recommended this exception is to be ignored or handled
    separatly in production.

    """



class WePayConnectionError(Exception):
    """Raised in case there is a problem connecting to WePay servers, for
    instance when request times out.

    """

    def __init__(self, error):
        self._error = error


    def __str__(self):
        return "%s - %s" % (self.error.__class__.__name__, self.error)


    @property
    def error(self):
        """Original exception raised by `urllib` or `requests` library. It will
        be either :exc:`urllib.error.URLError` or
        a subclass of :exc:`requests.exceptions.RequestExeption`. See their corresponding
        documentation if necessary.

        """
        return self._error


    @property
    def message(self):
        warnings.warn("'message' is deprecated",
                      DeprecationWarning)
        return str(self)

