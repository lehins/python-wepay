from api import WePay

# Major, minor, revision
VERSION = (1, 2, 1)

def get_version():
    return "%s.%s.%s" % VERSION

__version__ = get_version()
