#import unittest
#from mock import MagicMock
#from wepay import WePay
from wepay.tests import CallBaseTestCase

class AccountTestCase(CallBaseTestCase):

    def test_account(self):
        args = [
            ('account_id', 12345)
        ]
        kwargs = {}
        self._test_call('/account', args, kwargs)

    def test_account_find(self):
        args = []
        kwargs = {
            'name': 'Dummy Account',
            'reference_id': 'ref_1234',
            'sort_order': 'ASC',
        }
        self._test_call('/account/find', args, kwargs)

    def test_account_create(self):
        args = [
            ('name', 'Dummy Account'),
            ('description', 'Dummy Description')
        ]
        kwargs = {
            'reference_id': 'ref_1234',
            'type': 'business',
            'image_uri': "https://stage.wepay.com/img/logo.png",
            'gaq_domains': ['UA-23421-01', 'UA-23421-02'],
            'theme_object': {
                'name': 'dummy_name',
                'primary_color': "#FFFFFF",
                'secondary_color': "#FFFFFF",
                'background_color': "#FFFFFF",
                'button_color': "#FFFFFF"
            },
            'mcc': 7372,
            'callback_uri': 'https://example.com/callback',
            'country': "US",
            'currencies': ["USD"]
        }
        self._test_call('/account/create', args, kwargs)

    def test_account_modify(self):
        args = [
            ('account_id', 1234),
        ]
        kwargs = {
            'name': 'Dummy Account',
            'description': 'Dummy Description',
            'reference_id': 'ref_1234',
            'image_uri': "https://stage.wepay.com/img/logo.png",
            'gaq_domains': ['UA-23421-01', 'UA-23421-02'],
            'theme_object': {
                'name': 'dummy_name',
                'primary_color': "#FFFFFF",
                'secondary_color': "#FFFFFF",
                'background_color': "#FFFFFF",
                'button_color': "#FFFFFF"
            },
            'callback_uri': 'https://example.com/callback',
        }
        self._test_call('/account/modify', args, kwargs)

    def test_account_delete(self):
        args = [
            ('account_id', 1234),
        ]
        kwargs = {
            'reason': 'For no reason',
        }
        self._test_call('/account/delete', args, kwargs)

    def test_account_get_update_uri(self):
        args = [
            ('account_id', 1234),
        ]
        kwargs = {
            'mode': 'iframe',
            'redirect_uri': "https://example.com/redirect"
        }
        self._test_call('/account/get_update_uri', args, kwargs)

    def test_account_get_reserve_details(self):
        args = [
            ('account_id', 1234),
        ]
        kwargs = {
            'currency': 'USD',
        }
        self._test_call('/account/get_reserve_details', args, kwargs)
