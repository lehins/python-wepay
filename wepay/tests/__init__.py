import unittest
from mock import MagicMock
from wepay import WePay

class CallBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.api = WePay(silent=False)
        self.api.call = MagicMock()

    def _test_call(self, call, args, kwargs):
        path = call.split('/')[1:]
        fn = self.api
        for p in path:
            fn = getattr(fn, p)
        allowed_params = {x[0] for x in args}

        # test required params:
        fn(*[x[1] for x in args])
        self.api.call.assert_called_once_with(
            call, access_token=None, params=dict(args), api_version=None)
        if kwargs:
            # test with all optional params
            fn(*[x[1] for x in args], **kwargs)
            self.api.call.assert_called_oncewith(
                call, access_token=None, params=dict(args, **kwargs), api_version=None)
            allowed_params = allowed_params.union(kwargs)
        self.assertEqual(allowed_params, set(fn.allowed_params))

        