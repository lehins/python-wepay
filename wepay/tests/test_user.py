import unittest
from mock import MagicMock
from wepay import WePay

class UserTestCase(unittest.TestCase):

    def setUp(self):
        self.api = WePay(production=False)
        self.api.call = MagicMock()
        
    def test_user(self):
        self.api.user()
        self.api.call.assert_called_once_with(
            '/user', access_token=None, params={}, api_version=None)


    def test_user_modify(self):
        self.api.user.modify()
        self.api.call.assert_called_once_with(
            '/user/modify', access_token=None, params={}, api_version=None)
        kwargs = {
            'callback_uri': 'https://example.com/callback'
        }
        self.api.user.modify(**kwargs)
        self.api.call.assert_called_oncewith(
            '/user/modify', access_token=None, params=kwargs, api_version=None)


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
        self.api.user.register(*[x[1] for x in args])
        self.api.call.assert_called_once_with(
            '/user/register', access_token=None, params=dict(args), api_version=None)
        kwargs = {
            'redirect_uri': 'https://example.com/redirect',
            'callback_uri': 'https://example.com/callback'
        }
        self.api.user.register(*[x[1] for x in args], **kwargs)
        self.api.call.assert_called_oncewith(
            '/user/register', access_token=None, params=dict(args, **kwargs), api_version=None)

    def test_user_resend_confirmation(self):
        self.api.user.resend_confirmation()
        self.api.call.assert_called_once_with(
            '/user/resend_confirmation', access_token=None, params={}, api_version=None)
        kwargs = {
            'email_message': "Welcome to my <strong>application</strong>"
        }
        self.api.user.resend_confirmation(**kwargs)
        self.api.call.assert_called_oncewith(
            '/user/resend_confirmation', access_token=None, params=kwargs, api_version=None)
