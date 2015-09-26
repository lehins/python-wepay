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

    def test_user_send_confirmation(self):
        args = []
        kwargs = {
            'email_message': "Welcome to my <strong>application</strong>"
        }
        self._test_call('/user/send_confirmation', args, kwargs)

        
class UserMFATestCase(CallBaseTestCase):

    def test_user_mfa_create(self):
        args = [
            ('type', 'voice')
        ]
        kwargs = {
            'nickname': 'foobar',
            'setup_data': {
                'phone_number': "5055551234"
            },
            'cookie': "WSIG=Ap4P... .GTEq; Domain=foo.com; Path=/; Expires=Wed, " 
            "13 Jan 2015 22:23:01 GMT; Secure; HttpOnly"
        }
        self._test_call('/user/mfa/create', args, kwargs)

    def test_user_mfa_validate_cookie(self):
        args = [
            ('mfa_id', 1234),
            ('cookie', "WSIG=Ap4P... .GTEq; Domain=foo.com; Path=/; Expires=Wed, " 
             "13 Jan 2015 22:23:01 GMT; Secure; HttpOnly")
        ]
        kwargs = {}
        self._test_call('/user/mfa/validate_cookie', args, kwargs)

    def test_user_mfa_send_challenge(self):
        args = [
            ('mfa_id', 1234),
        ]
        kwargs = {
            'force_voice': True
        }
        self._test_call('/user/mfa/send_challenge', args, kwargs)

    def test_user_mfa_send_default_challenge(self):
        args = []
        kwargs = {}
        self._test_call('/user/mfa/send_default_challenge', args, kwargs)

    def test_user_mfa_confirm(self):
        args = [
            ('mfa_id', 1234),
            ('challenge', {
                "code": "456789", 
                "keep_session": True, 
                "cookie_domain": ".example.com", 
            })
        ]
        kwargs = {}
        self._test_call('/user/mfa/confirm', args, kwargs)

    def test_user_mfa_find(self):
        args = []
        kwargs = {
            'challenge': {
                "code": "456789", 
                "keep_session": True, 
                "cookie_domain": ".example.com", 
            }
        }
        self._test_call('/user/mfa/find', args, kwargs)

    def test_user_mfa_modify(self):
        args = [
            ('mfa_id', 1234),
        ]
        kwargs = {}
        self._test_call('/user/mfa/modify', args, kwargs)
