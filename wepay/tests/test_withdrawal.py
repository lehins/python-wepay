from wepay.tests import CallBaseTestCase

class WithdrawalTestCase(CallBaseTestCase):

    def test_withdrawal(self):
        args = [
            ('withdrawal_id', 12345)
        ]
        kwargs = {}
        self._test_call('/withdrawal', args, kwargs)

    def test_withdrawal_find(self):
        args = [
            ('account_id', 54321)
        ]
        kwargs = {
            'limit': 17,
            'start': 10,
            'sort_order': 'ASC'
        }
        self._test_call('/withdrawal/find', args, kwargs)

    def test_withdrawal_create(self):
        args = [
            ('account_id', 54321)
        ]
        kwargs = {
            'currency': 'USD',
            'redirect_uri': 'https://example.com/redirect',
            'callback_uri': 'https://example.com/callback',
            'fallback_uri': 'https://example.com/failback',
            'note': "A Short Description of the Withdrawal",
            'mode': 'iframe',
        }
        self._test_call('/withdrawal/create', args, kwargs)

    def test_withdrawal_modify(self):
        args = [
            ('withdrawal_id', 1234),
        ]
        kwargs = {
            'callback_uri': 'https://example.com/callback',
        }
        self._test_call('/withdrawal/modify', args, kwargs)
