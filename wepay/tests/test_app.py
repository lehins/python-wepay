import unittest
from mock import MagicMock
from wepay import WePay

class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.api = WePay(production=False)
        self.api.call = MagicMock()

    def test_app(self):
        args = [
            ('client_id', 12345),
            ('client_secret', 'secret_217'),
        ]
        self.api.app(*[x[1] for x in args])
        self.api.call.assert_called_once_with(
            '/app', access_token=None, params=dict(args), api_version=None)


    def test_app_modify(self):
        args = [
            ('client_id', 12345),
            ('client_secret', 'secret_217')
        ]
        kwargs = {
            'theme_object': {
                'name': 'dummy_name',
                'primary_color': "#FFFFFF",
                'secondary_color': "#FFFFFF",
                'background_color': "#FFFFFF",
                'button_color': "#FFFFFF"
            },
            'gaq_domains': ['UA-23421-01', 'UA-23421-02']
        }
        self.api.app.modify(*[x[1] for x in args])
        self.api.call.assert_called_once_with(
            '/app/modify', access_token=None, params=dict(args), api_version=None)
        self.api.app.modify(*[x[1] for x in args], **kwargs)
        self.api.call.assert_called_oncewith(
            '/app/modify', access_token=None, params=dict(args, **kwargs), api_version=None)

