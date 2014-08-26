
__all__ = [
    'WePayWarning', 'WePayError', 'WePayHTTPError', 'WePayClientError',
    'WePayServerError', 'WePayConnectionError'
]



class WePayWarning(UserWarning):
    pass
    


class WePayError(Exception):
    """Raised whenever WePay API call was not successfull. `WePay API Errors
    Documentation <https://www.wepay.com/developer/reference/errors>`_

    """
    def __init__(self, error, error_code, error_description):
        self._error = error
        self._error_code = error_code
        self._error_description = error_description


    def __str__(self):
        return "%s (%s): %s" % (self.error, self.error_code, self.error_description)

    @property
    def error(self):
        """Generic ``error`` category. Returned by WePay."""
        return self._error


    @property
    def error_code(self):
        """A specific "error_code" that you can use to program responses to
        errors. Returned by WePay.

        """
        return self._error_code


    @property
    def error_description(self):
        """A human readable ``error_description`` that explains why the error
        happened. Returned by WePay.

        """
        return self._error_description



class WePayHTTPError(WePayError):
    """This is a base http error"""

    def __init__(self, http_error, status_code, 
                 error=None, error_code=None, error_description=None):
        self._http_error = http_error
        self._status_code = status_code
        error = error or 'unknown'
        error_code = error_code or -1
        error_description = error_description or "Unknown"
        super(WePayHTTPError, self).__init__(error, error_code, error_description)


    def __str__(self):
        return "HTTP %s - %s" % (
            self.status_code, super(WePayHTTPError, self).__str__())


    @property
    def status_code(self):
        """Error Code as specified by RFC 2616."""
        return self._status_code


    @property
    def http_error(self):
        """Instance of :exc:`urllib.error.HTTPError` or
        :exc:`requests.exceptions.HTTPError`, depending on the library you chose.

        """
        return self._http_error



class WePayClientError(WePayHTTPError):
    """This is a 4xx type error, which, most of the time, carries important
    information about the object of interest.

    """



class WePayServerError(WePayHTTPError):
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
        return "%s - %s" % (self.error.__class__.__name__, str(self.error))


    @property
    def error(self):
        """Original exception raised by `urllib` or `requests` library. It will
        be either :exc:`urllib.error.URLError` or
        a subclass of :exc:`requests.exceptions.RequestExeption`. See their corresponding
        documentation if necessary.

        """
        return self._error
