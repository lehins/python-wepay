import unittest, warnings, requests
from mock import MagicMock
from six.moves import urllib
from wepay import WePay
from wepay.exceptions import *

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.api = WePay(production=False)


    def test_uris_production(self):
        api = WePay()
        self.assertEqual(api.api_endpoint,
                         "https://wepayapi.com/v2")
        self.assertEqual(api.browser_uri,
                         "https://www.wepay.com")
        self.assertEqual(api.browser_js,
                         "https://www.wepay.com/min/js/wepay.v2.js")
        self.assertEqual(api.browser_iframe_js,
                         "https://www.wepay.com/min/js/iframe.wepay.js")
        self.assertEqual(api.browser_endpoint,
                         "https://www.wepay.com/v2")        


    def test_uris(self):
        self.assertEqual(self.api.api_endpoint,
                         "https://stage.wepayapi.com/v2")
        self.assertEqual(self.api.browser_uri,
                         "https://stage.wepay.com")
        self.assertEqual(self.api.browser_js,
                         "https://stage.wepay.com/js/wepay.v2.js")
        self.assertEqual(self.api.browser_iframe_js,
                         "https://stage.wepay.com/js/iframe.wepay.js")
        self.assertEqual(self.api.browser_endpoint,
                         "https://stage.wepay.com/v2")

        
    def test_call(self):
        self.assertRaises(WePayError, self.api.call, '/app')


    def test_error(self):
        try:
            self.api.call('/foo')
        except WePayServerError as e:
            self.assertIsInstance(e.http_error, requests.exceptions.HTTPError)
            self.assertEqual(e.status_code, 501)
            self.assertEqual(e.error, "invalid_request")
            self.assertEqual(e.error_code, 1001)
            self.assertEqual(e.error_description, 
                             "that is not a recognized WePay API call")
            self.assertEqual(str(e), "HTTP 501 - invalid_request (1001): "
                             "that is not a recognized WePay API call")


    def test_silent_and_warnings(self):
        # production=False, silent=None or False -> raises WePayWarning
        self.assertRaises(WePayWarning, self.api.user.modify, foo='bar')
        # production=True or False, silent=True -> suppresses param check completely
        api = WePay(production=False, silent=True)
        self.assertRaises(WePayError, api.user.modify, foo='bar')
        # production=True, silent=None -> prints warning and will raise WePayError
        api = WePay(production=True)
        api.call = MagicMock()
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            api.user.modify(foo='bar')
            self.assertEqual(len(w), 1)
            self.assertIs(w[-1].category, WePayWarning)
        # production=True, silent=False -> raises WePayWarning
        api = WePay(production=True, silent=False)
        api.call = MagicMock()
        self.assertRaises(WePayWarning, api.user.modify, foo='bar')


    def test_urllib(self):
        api = WePay(production=False, use_requests=False)
        self.assertRaises(WePayError, api.call, '/app')
        try:
            api.call('/app')
        except WePayClientError as e:
            self.assertIsInstance(e.http_error, urllib.error.HTTPError)
            self.assertEqual(e.status_code, 400)
            self.assertEqual(e.error, "invalid_request")
            self.assertEqual(e.error_code, 1004)
            self.assertEqual(e.error_description, "client_id parameter is required")


    def test_requests_missing(self):
        from wepay import utils
        has_requests = utils.HAS_REQUESTS
        utils.HAS_REQUESTS = False
        # test the warning, if requests are misiing
        self.assertRaises(WePayWarning, WePay, 
                          production=False, use_requests=True, silent=False)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            WePay(production=False, use_requests=True)
            self.assertEqual(len(w), 1)
            self.assertIs(w[-1].category, WePayWarning)
        utils.HAS_REQUESTS = has_requests


    def test_urllib_connection_error(self):
        api = WePay(production=False, use_requests=False, timeout=0.001)
        self.assertRaises(WePayConnectionError, api.call, '/app')
        try:
            api.call('/app')
        except WePayConnectionError as e:
            self.assertIsInstance(e.error, urllib.error.URLError)
            self.assertEqual(str(e), "URLError - <urlopen error timed out>")
                          

    def test_requests_connection_error(self):
        try:
            self.api.call('/app', timeout=0.001)
        except WePayConnectionError as e:
            self.assertIsInstance(e.error, requests.exceptions.Timeout)


    def test_headers(self):
        api = WePay(production=False)
        api._post = MagicMock()
        api._post.configure_mock(**{'__call__': {'result': 'fake_success'}})
        access_token, api_version = 'dummy_access_token', '2011-01-15'
        expected_headers = {
            'Content-Type': 'application/json', 
            'User-Agent': 'Python WePay SDK (third party)',
            'Authorization': 'Bearer %s' % access_token,
            'Api-Version': api_version
          }
        api.call('/user', access_token=access_token, api_version=api_version)
        api._post.assert_called_once_with(
            'https://stage.wepayapi.com/v2/user', {}, expected_headers, 30)

