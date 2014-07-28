import unittest
from mock import MagicMock
from wepay import WePay

class CallBaseTestCase(unittest.TestCase):

    def setUp(self):
        self.api = WePay(silent=False)
        self.api.call = MagicMock()

    def _test_call(self, call, args, kwargs, **control_kwargs):
        path = call.split('/')[1:]
        fn = self.api
        for p in path:
            fn = getattr(fn, p)
        allowed_params = {x[0] for x in args}

        # test required params:
        fn(*[x[1] for x in args], **control_kwargs)
        self.api.call.assert_called_once_with(
            call, params=dict(args), **control_kwargs)
        if kwargs:
            self.api.call.reset_mock()
            # test with all optional params
            ks = kwargs.copy()
            ks.update(control_kwargs)
            fn(*[x[1] for x in args], **ks)
            self.api.call.assert_called_once_with(
                call, params=dict(args, **kwargs), **control_kwargs)
            allowed_params = allowed_params.union(kwargs)
        self.assertEqual(allowed_params, set(fn.allowed_params))

        