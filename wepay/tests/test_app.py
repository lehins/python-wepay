from wepay.tests import CallBaseTestCase

class AppTestCase(CallBaseTestCase):

    def test_app(self):
        args = [
            ('client_id', 12345),
            ('client_secret', 'secret_217'),
        ]
        self._test_call('/app', args, {})


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
        self._test_call('/app/modify', args, kwargs)
      
