from wepay.tests import CallBaseTestCase

class PreapprovalTestCase(CallBaseTestCase):

    def test_preapproval(self):
        args = [
            ('preapproval_id', 12345)
        ]
        kwargs = {}
        self._test_call('/preapproval', args, kwargs)

    def test_preapproval_find(self):
        args = []
        kwargs = {
            'account_id': 54321,
            'state': 'expired',
            'reference_id': 'ref_preapproval_123',
            'start': 10,
            'limit': 17,
            'sort_order': 'ASC',
            'last_checkout_id': 221651,
            'shipping_fee': 34.05
        }
        self._test_call('/preapproval/find', args, kwargs)

    def test_preapproval_create(self):
        args = [
            ('short_description', "Dummy Preapproval Description"),
            ('period', 'weekly')
        ]
        kwargs = {
            # these should be passed for app level preapprovals, 
            # instead of account_id and access_token
            'client_id': 67890, 
            'client_secret': 'secret_9876',

            'account_id': 54321,
            'amount': 57.90,
            'currency': 'USD',
            'reference_id': "preapproval_ref_321",
            'app_fee': 2.43,
            'fee_payer': 'payer_from_app',
            'redirect_uri': 'https://example.com/redirect',
            'callback_uri': 'https://example.com/callback',
            'fallback_uri': 'https://example.com/failback',
            'require_shipping': True,
            'shipping_fee': 54.76,
            'charge_tax': True,
            'payer_email_message': "Payer Message.",
            'long_description': "Very Long Dummy Description.",
            'frequency': 2,
            'start_time': 1398211651,
            'end_time': 1398221651,
            'auto_recur': True,
            'mode': 'iframe',
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
        self._test_call('/preapproval/create', args, kwargs)

    def test_preapproval_cancel(self):
        args = [
            ('preapproval_id', 1234),
        ]
        kwargs = {}
        self._test_call('/preapproval/cancel', args, kwargs)

    def test_preapproval_modify(self):
        args = [
            ('preapproval_id', 1234),
        ]
        kwargs = {
            'callback_uri': 'https://example.com/callback',
        }
        self._test_call('/preapproval/modify', args, kwargs)
