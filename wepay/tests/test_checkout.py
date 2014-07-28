import decimal
from wepay.tests import CallBaseTestCase

class CheckoutTestCase(CallBaseTestCase):

    def test_checkout(self):
        args = [
            ('checkout_id', 12345)
        ]
        kwargs = {}
        self._test_call('/checkout', args, kwargs)

    def test_checkout_find(self):
        args = [
            ('account_id', 54321)
        ]
        kwargs = {
            'start': 10,
            'limit': 17,
            'reference_id': 'ref_checkout_123',
            'state': 'expired',
            'preapproval_id': 56789,
            'start_time': 1398211651,
            'end_time': 1398221651,
            'sort_order': 'ASC',
            'shipping_fee': decimal.Decimal('34.05')
        }
        self.api.checkout.find(*[x[1] for x in args])
        self.api.call.assert_called_once_with('/checkout/find', params=dict(args))
        # test conversion from decimal
        self.api.call.reset_mock()
        self.api.checkout.find(*[x[1] for x in args], **kwargs)
        kwargs = kwargs.copy()
        kwargs['shipping_fee'] = float(kwargs['shipping_fee'])
        self.api.call.assert_called_once_with(
            '/checkout/find', params=dict(args, **kwargs))


    def test_checkout_create(self):
        args = [
            ('account_id', 54321),
            ('short_description', "Dummy Checkout Description"),
            ('type', 'EVENT'),
            ('amount', 57.90)
        ]
        kwargs = {
            'currency': 'USD',
            'long_description': "Very Long Dummy Description.",
            'payer_email_message': "Payer Message.",
            'payee_email_message': "Payee Message.",
            'reference_id': "checkout_ref_321",
            'app_fee': 2.43,
            'fee_payer': 'payer_from_app',
            'redirect_uri': 'https://example.com/redirect',
            'callback_uri': 'https://example.com/callback',
            'fallback_uri': 'https://example.com/failback',
            'auto_capture': False,
            'require_shipping': True,
            'shipping_fee': 54.76,
            'charge_tax': True,
            'mode': 'iframe',
            'preapproval_id': 7654,
            'prefill_info': {
                'name':"Foo Bar",
                'email': "foo@example.com",
                'phone_number':'855-469-3729',
                'address': "123 Main St.",
                'city': "Albuquerque",
                'state': "NM",
                'region': "non-US region, Mexico? :)",
                'zip': 87102,
                'postcode': "non-US Postcode",
                'country': "US"
            },
            'funding_sources': 'bank,cc',
            'payment_method_id': 87600,
            'payment_method_type': 'credit_card'
        }
        self._test_call('/checkout/create', args, kwargs)

    def test_checkout_cancel(self):
        args = [
            ('checkout_id', 1234),
            ('cancel_reason', "Dummy Checkout Cancel Reason."),
        ]
        kwargs = {}
        self._test_call('/checkout/cancel', args, kwargs)

    def test_checkout_refund(self):
        args = [
            ('checkout_id', 1234),
            ('refund_reason', "Dummy Checkout Refund Reason."),
        ]
        kwargs = {
            'amount': 43.78,
            'app_fee': 3.78,
            'payer_email_message': "Dummy Payer Email Message",
            'payee_email_message': "Dummy Payee Email Message."
        }
        self._test_call('/checkout/refund', args, kwargs)

    def test_checkout_capture(self):
        args = [
            ('checkout_id', 1234),
        ]
        kwargs = {}
        self._test_call('/checkout/capture', args, kwargs)

    def test_checkout_modify(self):
        args = [
            ('checkout_id', 1234),
        ]
        kwargs = {
            'callback_uri': 'https://example.com/callback',
        }
        self._test_call('/checkout/modify', args, kwargs)
