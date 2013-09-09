
class WePayError(Exception):
    def __init__(self, error_type, message, error_code=None):
        self.type = error_type
        self.code = error_code
        super(WePayError, self).__init__(message)

