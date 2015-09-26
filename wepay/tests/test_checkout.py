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
            'email_message': {
                'to_payee': "Payee Message.",
                'to_payer': "Payer Message."                
            },
            'fee': {
                'app_fee': 2.43,
                'fee_payer': 'payer_from_app'                
            },
            'callback_uri': 'https://example.com/callback',
            'auto_capture': False,
            'reference_id': "checkout_ref_321",
            'unique_id': 987654321,
            'hosted_checkout': {
                'redirect_uri': 'https://example.com/redirect',
                'mode': 'iframe',
                'fallback_uri': 'https://example.com/failback',
                'shipping_fee': 54.76,
                'require_shipping': True,
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
                'funding_sources': ['credit_card', 'bank_account'],
                'theme_object': {
                    "name": "test",
                    "primary_color": "ffffff",
                    "background_color": "ffffff",
                    "button_color": "000000",
                    "secondary_color": "000000"
                }                
            },
            'payment_method': {
                'type': 'preapproval',
                'preapproval': {
                    'id': 7654
                }
            },
            'delivery_type': 'full_prepayment'
        }
        self._test_call('/checkout/create', args, kwargs, exclude=[
            'payer_email_message', 'payee_email_message', 'app_fee', 'fee_payer',
            'redirect_uri', 'fallback_uri', 'require_shipping',
            'shipping_fee', 'mode', 'preapproval_id', 'prefill_info',
            'funding_sources', 'payment_method_id', 'payment_method_type'
        ])
        
    def test_checkout_create_old(self):
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
            'payment_method_type': 'credit_card',
            'unique_id': 987654321
        }
        self._test_call('/checkout/create', args, kwargs, exclude=[
            'email_message', 'fee', 'hosted_checkout', 'payment_method',
            'delivery_type'
        ])

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
