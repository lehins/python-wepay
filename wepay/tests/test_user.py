from wepay.tests import CallBaseTestCase

class UserTestCase(CallBaseTestCase):

    def test_user(self):
        self._test_call('/user', [], {})

    def test_user_modify(self):
        args = []
        kwargs = {
            'callback_uri': 'https://example.com/callback'
        }
        self._test_call('/user/modify', args, kwargs)

    def test_user_register(self):
        args = [
            ('client_id', 12345),
            ('client_secret', '6446c521bd'),
            ('email', 'api@wepay.com'),
            ('scope', 'manage_accounts,view_balance,collect_payments,view_user'),
            ('first_name', 'Bill'),
            ('last_name', 'Clerico'),
            ('original_ip', '74.125.224.84'),
            ('original_device', ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6;"
                                 "en-US) AppleWebKit/534.13 (KHTML, like Gecko)"
                                 "Chrome/9.0.597.102 Safari/534.13"))
        ]
        kwargs = {
            'redirect_uri': 'https://example.com/redirect',
            'callback_uri': 'https://example.com/callback',
            'tos_acceptance_time': 1398211651
        }
        self._test_call('/user/register', args, kwargs)

    def test_user_resend_confirmation(self):
        args = []
        kwargs = {
            'email_message': "Welcome to my <strong>application</strong>"
        }
        self._test_call('/user/resend_confirmation', args, kwargs)
