from wepay.tests import CallBaseTestCase

class Subscription_ChargeTestCase(CallBaseTestCase):

    def test_subscription_charge(self):
        args = [
            ('subscription_charge_id', 12345)
        ]
        kwargs = {}
        self._test_call('/subscription_charge', args, kwargs)

    def test_subscription_charge_find(self):
        args = [
            ('subscription_id', 12345)
        ]
        kwargs = {
            'start': 10,
            'limit': 17,
            'start_time': 1398211651,
            'end_time': 1398221651,
            'type': 'setup_fee',
            'amount': 54,
            'state': 'failed',
        }
        self._test_call('/subscription_charge/find', args, kwargs)


    def test_subscription_charge_refund(self):
        args = [
            ('subscription_charge_id', 1234)
        ]
        kwargs = {
            'refund_reason': "Dummy Subscription Charge Refund Reason."
        }
        self._test_call('/subscription_charge/refund', args, kwargs)


