from api import WePay

# Major, minor, revision
VERSION = (1, 2, 3)

def get_version():
    return "%s.%s.%s" % VERSION

__version__ = get_version()
