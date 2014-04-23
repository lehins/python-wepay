from wepay.tests import CallBaseTestCase

class SubscriptionTestCase(CallBaseTestCase):

    def test_subscription(self):
        args = [
            ('subscription_id', 12345)
        ]
        kwargs = {}
        self._test_call('/subscription', args, kwargs)

    def test_subscription_find(self):
        args = [
            ('subscription_plan_id', 12345)
        ]
        kwargs = {
            'start': 10,
            'limit': 17,
            'start_time': 1398211651,
            'end_time': 1398221651,
            'state': 'active',
            'reference_id': 'ref_subscription_123'
        }
        self._test_call('/subscription/find', args, kwargs)

    def test_subscription_create(self):
        args = [
            ('subscription_plan_id', 54321),
        ]
        kwargs = {
            'redirect_uri': 'https://example.com/redirect',
            'callback_uri': 'https://example.com/callback',
            'payment_method_id': 87600,
            'payment_method_type': 'credit_card',
            'mode': 'regular',
            'quantity': 3,
            'reference_id': "subscription_ref_321",
            'prefill_info': {
                'name':"Bugs Bunny",
                'email': "loony@tunes.com",
                'phone_number':'855-469-3729',
                'address': "123 Main St.",
                'city': "Albuquerque",
                'state': "NM",
                'zip': 87102,
                'country': "US"
            },
        }
        self._test_call('/subscription/create', args, kwargs)

    def test_subscription_cancel(self):
        args = [
            ('subscription_id', 1234)
        ]
        kwargs = {
            'reason': "Dummy Subscription Cancel Reason."
        }
        self._test_call('/subscription/cancel', args, kwargs)


    def test_subscription_modify(self):
        args = [
            ('subscription_id', 54321)
        ]
        kwargs = {
            'subscription_plan_id': 54321,
            'quantity': 3,
            'prorate': True,
            'transition_expire_days': 7,
            'redirect_uri': 'https://example.com/redirect',
            'callback_uri': 'https://example.com/callback',
            'payment_method_id': 87600,
            'payment_method_type': 'credit_card',
            'reference_id': 'subscription_ref_321',
            'extend_trial_days': 4
        }
        self._test_call('/subscription/modify', args, kwargs)
