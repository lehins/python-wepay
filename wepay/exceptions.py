
class WePayError(Exception):
    """Raised in case API call was not successfull.
    `WePay API Errors Documantation <https://www.wepay.com/developer/reference/errors>`_
    """
    def __init__(self, error_type, message, error_code=None):
        self.error = error_type
        self.code = error_code
        super(WePayError, self).__init__(message)

    def __str__(self):
        return "%s (%s): %s" % (self.error, self.code, self.message)
