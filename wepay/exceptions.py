
class WePayError(Exception):
    """Raised in case API call was not successfull.  `WePay API Errors Documantation
    <https://www.wepay.com/developer/reference/errors>`_

    """
    def __init__(self, error_type, message, error_code=None):
        self._error = error_type
        self._code = error_code
        self._message = message
        super(WePayError, self).__init__()

    @property
    def error(self):
        """``error`` parameter return from WePay: `possible values
        <https://www.wepay.com/developer/reference/errors>`_
        
        """
        return self._error

    @property
    def code(self):
        """``error_code`` parameter return from WePay: `possible values
        <https://www.wepay.com/developer/reference/errors>`_
        
        """
        return self._code

    @property
    def message(self):
        """``error_description`` that corresspond to the ``error_code`` parameter.

        """
        return self._message

    def __str__(self):
        return "%s (%s): %s" % (self.error, self.code, self.message)
