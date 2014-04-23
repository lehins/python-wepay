from wepay.tests import CallBaseTestCase

class SubscriptionPlanTestCase(CallBaseTestCase):

    def test_subscription_plan(self):
        args = [
            ('subscription_plan_id', 12345)
        ]
        kwargs = {}
        self._test_call('/subscription_plan', args, kwargs)

    def test_subscription_plan_find(self):
        args = []
        kwargs = {
            'account_id': 54321,
            'start': 10,
            'limit': 17,
            'state': 'expired',
            'reference_id': 'ref_subscription_plan_123'
        }
        self._test_call('/subscription_plan/find', args, kwargs)

    def test_subscription_plan_create(self):
        args = [
            ('account_id', 54321),
            ('name', "Dummy Subscription Plan"),
            ('short_description', "Dummy Subscription_Plan Description"),
            ('amount', 57.90),
            ('period', 'yearly')
        ]
        kwargs = {
            'currency': 'USD',
            'app_fee': 4.54,
            'callback_uri': 'https://example.com/callback',
            'trial_length': 3,
            'setup_fee': 2.43,
            'reference_id': 'subscription_plan_ref_321',
        }
        self._test_call('/subscription_plan/create', args, kwargs)

    def test_subscription_plan_delete(self):
        args = [
            ('subscription_plan_id', 1234)
        ]
        kwargs = {
            'reason': "Dummy Subscription_Plan Delete Reason."
        }
        self._test_call('/subscription_plan/delete', args, kwargs)

    def test_subscription_plan_get_button(self):
        args = [
            ('account_id', 12345),
            ('button_type', 'subscription_all_plans'),
        ]
        kwargs = {
            'subscription_plan_id': 1234,
            'button_text': "Dummy Subscription",
            'button_options': {
                'show_plan_price': True,
                'show_plans': True, 
                'reference_id': 'ref_button_subscription_plan_123456'
            }
        }
        self._test_call('/subscription_plan/get_button', args, kwargs)

    def test_subscription_plan_modify(self):
        args = [
            ('subscription_plan_id', 54321)
        ]
        kwargs = {
            'name': "Dummy Subscription Plan",
            'short_description': "Dummy Subscription_Plan Description",
            'amount': 27.90,
            'app_fee': 4.54,
            'callback_uri': 'https://example.com/callback',
            'trial_length': 3,
            'setup_fee': 2.43,
            'update_subscriptions': 'paying_lower',
            'transition_expire_days': 5,
            'reference_id': 'subscription_plan_ref_321'
        }
        self._test_call('/subscription_plan/modify', args, kwargs)
