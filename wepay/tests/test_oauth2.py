from wepay.tests import CallBaseTestCase

class OAuth2TestCase(CallBaseTestCase):

    def test_authorize(self):
        self.assertEqual(self.api.oauth2.authorize(
            12345, 'https://example.com/wepay', "manage_accounts,collect_payments",
            state='stateless', user_name='foo', user_email='foo@example.com'),
                         "https://www.wepay.com/v2/oauth2/authorize"
                         "?client_id=12345"
                         "&redirect_uri=https%3A%2F%2Fexample.com%2Fwepay"
                         "&scope=manage_accounts%2Ccollect_payments"
                         "&user_name=foo"
                         "&user_email=foo%40example.com"
                         "&state=stateless")


    def test_token(self):
        args = [
            ('client_id', 12345),
            ('redirect_uri', 'https://example.com/wepay'), 
            ('client_secret', 'secret_217'),
            ('code', 'code_317') 
        ]
        kwargs = {
            'callback_uri': 'https://example.com/wepay/callback/'
        }
        self._test_call('/oauth2/token', args, kwargs)

    def test_token_batch_mode(self):
        kwargs = {
            'client_id': 12345,
            'redirect_uri': 'https://example.com/wepay', 
            'client_secret': 'secret_217',
            'code': 'code_317',
            'callback_uri': 'https://example.com/wepay/callback/'
        }
        self.assertEqual(self.api.oauth2.token(
            batch_mode=True, batch_reference_id='batch_417', **kwargs),
                         {'call': '/oauth2/token',
                          'reference_id':'batch_417',
                          'parameters': kwargs})