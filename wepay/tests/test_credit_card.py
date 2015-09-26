from wepay.tests import CallBaseTestCase

class Credit_CardTestCase(CallBaseTestCase):

    def test_credit_card(self):
        args = [
            ('client_id', 7654),
            ('client_secret', 'secret_9876543'),
            ('credit_card_id', 12345)
        ]
        kwargs = {}
        self._test_call('/credit_card', args, kwargs)

    def test_credit_card_create(self):
        args = [
            ('client_id', 54321),
            ('cc_number', '4003830171874018'),
            ('cvv', 911),
            ('expiration_month', 4),
            ('expiration_year', 2014),
            ('user_name', "Joe Blow"),
            ('email', 'joe@example.com'),
            ('address', {
                'name':"Foo Bar",
                'email': "foo@example.com",
                'phone_number':'855-469-3729',
                'address': "123 Main St.",
                'city': "Albuquerque",
                'state': "NM",
                'region': "non-US region, Mexico? :)",
                'zip': 87102,
                'postcode': "non-US Postcode",
                'country': "US"
            })
        ]
        kwargs = {
            'reference_id': "credit_card_reference_id_765", # UNDOCUMENTED
            'original_ip': '74.125.224.84',
            'original_device': ("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6;"
                                "en-US) AppleWebKit/534.13 (KHTML, like Gecko)"
                                "Chrome/9.0.597.102 Safari/534.13"),
            'auto_update': True
        }
        self._test_call('/credit_card/create', args, kwargs)

    def test_credit_card_authorize(self):
        args = [
            ('client_id', 12345),
            ('client_secret', 'secret_54321'),
            ('credit_card_id', 1234)
        ]
        kwargs = {}
        self._test_call('/credit_card/authorize', args, kwargs)

    def test_credit_card_find(self):
        args = [
            ('client_id', 12345),
            ('client_secret', 'secret_54321')
        ]
        kwargs = {
            'reference_id': "ref_1234",
            'limit': 10,
            'start': 5,
            'sort_order': 'ASC'
        }
        self._test_call('/credit_card/find', args, kwargs)

    def test_credit_card_delete(self):
        args = [
            ('client_id', 12345),
            ('client_secret', 'secret_54321'),
            ('credit_card_id', 1234)
        ]
        kwargs = {}
        self._test_call('/credit_card/delete', args, kwargs)
        
    def test_credit_card_transfer(self):
        args = [
            ('client_id', 54321),
            ('client_secret', 'secret_54321'),
            ('cc_number', '4003830171874018'),
            ('expiration_month', 9),
            ('expiration_year', 2015),
            ('user_name', "Joe Blow"),
            ('email', 'joe@example.com'),
            ('address', {
                'name':"Foo Bar",
                'email': "foo@example.com",
                'phone_number':'855-469-3729',
                'address': "123 Main St.",
                'city': "Albuquerque",
                'state': "NM",
                'region': "non-US region, Mexico? :)",
                'zip': 87102,
                'postcode': "non-US Postcode",
                'country': "US"
            })
        ]
        kwargs = {
            'reference_id': "credit_card_reference_id_765",
        }
        self._test_call('/credit_card/transfer', args, kwargs)
