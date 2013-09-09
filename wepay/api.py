import urllib, urllib2, json, decimal, warnings

from wepay.exceptions import WePayError

__all__ = ["WePay"]

class WePayWarning(Warning):
    pass

class WePay(object):

    """
    A full client for the WePay API.
    """
    
    def __init__(self, production=True, access_token=None):
        """
        :param bool production: When ``False``, the ``stage.wepay.com`` API
            server will be used instead of the default production.
        :param str access_token: The access token associated with your
            application.
        """
        self.access_token = access_token
        if production:
            self.api_endpoint = "https://wepayapi.com/v2"
            self.browser_endpoint = "https://www.wepay.com/v2"
        else:
            self.api_endpoint = "https://stage.wepayapi.com/v2"
            self.browser_endpoint = "https://stage.wepay.com/v2"
    

    def call(self, uri, params=None, access_token=None, token=None):
        """
        Same call function as in Python-SDK WePay API with some minor changes. 
        Decimal numbers are casted to float, header is changed to
        'Python WePay SDK (third party)' 
        which also includes and error_code.
        Basically this is the place for all api calls.
        :param uri: API uri to call
        :type uri: string
        :param params: parameters to include in the call
        :type params: dict
        :param access_token: access_token to use for the call.
        :type access_token: string
        :param token: only here for compatibility with official Python WePay SDK.
        :type token: string
        """
        headers = {
            'Content-Type': 'application/json', 
            'User-Agent': 'Python WePay SDK (third party)'
        }
        url = self.api_endpoint + uri
        if not token is None:
            warnings.warn("'token' parameter is deprecated and is here only "
                          "for compatibility with official Python WePay SDK. "
                          "Use 'access_token' instead.", DeprecationWarning)
        access_token = access_token or token or self.access_token
        headers['Authorization'] = 'Bearer %s' % access_token
            
        if params:
            for key, value in params.iteritems():
                if isinstance(params[key], decimal.Decimal):
                    params[key] = float(params[key])
            params = json.dumps(params)

        request = urllib2.Request(url, params, headers)
        try:
            response = urllib2.urlopen(request, timeout=30).read()
            return json.loads(response)
        except urllib2.HTTPError as e:
            response = json.loads(e.read())
            raise WePayError(response['error'], response['error_description'], 
                             response['error_code'])
       
    def get_authorization_url(self, redirect_uri, client_id, options=None,
                              scope=None):
        """
        It is here for compatibilty with official Python WePay SDK        
        :param str redirect_uri: The URI to redirect to after a authorization.
        :param str client_id: The client ID issued by WePay to your app.
        :keyword dict options: Allows for passing additional values to the
            authorize call, aside from scope, redirect_uri, and etc.
        :keyword str scope: A comma-separated string of permissions.
        """
        warnings.warn("'get_authorization_url' is deprecated and is here only "
                      "for compatibility with official Python WePay SDK. "
                      "Use 'WePay.oauth2_authorize' instead.", DeprecationWarning)
        if not options:
            options = {}
        if not scope:
            scope = "manage_accounts,collect_payments,view_balance,view_user," \
                    "refund_payments"
        return self.oauth2_authorize(client_id, redirect_uri, scope, **options)
    
    def get_token(self, *args, **kwargs):
        """
        It is here for compatibilty with official Python WePay SDK
        """
        warnings.warn("'get_token' is deprecated and is here only "
                      "for compatibility with official Python WePay SDK. "
                      "Use 'WePay.oauth2_token' instead.", DeprecationWarning)
        response = self.oauth2_token(*args, **kwargs)
        self.access_token = response['access_token']
        return response

    def make_call(self, uri, params={}, allowed_params=[]):
        access_token = params.pop('access_token', self.access_token)
        batch_mode = params.pop('batch_mode', False)
        unrecognized_params = set(params) - set(allowed_params)
        if unrecognized_params:
            warnings.warn(
                "At least one of the parameters to the api call: '%s' is "
                "unrecognized. Allowed parameters are: '%s'. Unrecognized "
                "parameters are: '%s'." % 
                (uri, ', '.join(allowed_params), ', '.join(unrecognized_params)), 
                WePayWarning)
        if batch_mode:
            call = {
                'call': uri
            }
            if not access_token is None:
                call['authorization'] = access_token
            if params:
                call['parameters'] = params
            return call
        return self.call(uri, params=params, access_token=access_token)

    def oauth2_authorize(self, client_id, redirect_uri, scope, 
                         state=None, user_name=None, user_email=None):
        """
        This is the endpoint that you send the user to so they can grant your application permission to make calls on their behalf. It is not an API call but an actual uri that you send the user to. You can either do a full redirect to this uri OR if you want to keep the user on your site, you can open the uri in a popup with our JS library.
        This method provides a full redirect option.
        The easiest implementation for OAuth2 is to redirect the user to WePay's OAuth2 authorization uri. The following parameters should be uri encoded to the endpoint uri:
        :param client_id: The client id issued to the app, found on your application's dashboard.
        :type client_id: int
        :param redirect_uri: The uri the user will be redirected to after authorization. Must have the same domain as the application.
        :type redirect_uri: string
        :param scope: A comma separated string list of permissions. Click here for a list of permissions.
        :type scope: string
        :param state: The opaque value the client application uses to maintain state.
        :type state: string
        :param user_name: The user name used to pre-fill the authorization form
        :type user_name: string
        :param user_email: The user email used to pre-fill the authorization form
        :type user_email: string
        :returns: string -- uri with the request parameters uri encoded.
        """

        options = {
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'scope': scope
        }
        if not user_name is None:
            options['user_name'] = user_name
        if not user_email is None:
            options['user_email'] = user_email
        if not state is None:
            options['state'] = state
        return '%s/oauth2/authorize?%s' % (
            self.browser_endpoint, urllib.urlencode(options))

    def oauth2_token(self, client_id, redirect_uri, client_secret, code, **kwargs):
        """
        Once you have sent the user through the authorization end point and they have returned with a code, you can use that code to retrieve an access token for that user. The redirect uri will need to be the same as in the in :func:`~djwepay.core.OAuth2.authorize` step
        Note that when you request a new access_token with this call, we will automatically revoke all previously issued access_token for this user. Make sure you update the access_token you are using for a user each time you make this call.
        """
        allowed_params = [
            'client_id', 'redirect_uri', 'client_secret', 'code', 'callback_uri',
        ]
        params = {
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'client_secret': client_secret,
            'code': code
        }
        params.update(kwargs)
        return self.make_call(
            '/oauth2/token', params=params, allowed_params=allowed_params)

    def app(self, client_id, client_secret, **kwargs):
        allowed_params = ['client_id', 'client_secret']
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        params.update(kwargs)
        return self.make_call('/app', params=params, allowed_params=allowed_params)

    def app_modify(self, client_id, client_secret, 
                   theme_object=None, gaq_domains=None):
        allowed_params = [
            'client_id', 'client_secret', 'theme_object', 'gaq_domains'
        ]
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        return self.make_call('/app/modify', params, allowed_params=allowed_params)

    def user(self, **kwargs):
        return self.make_call('/user', params=kwargs)

    def user_modify(self, **kwargs):
        allowed_params = ['callback_uri']
        return self.make_call(
            '/user/modify', params=kwargs, allowed_params=allowed_params)

    def user_register(self, *args, **kwargs):
        raise NotImplementedError(
            "'/user/register' call is depricated and is not supported by this app")

    def user_resend_confirmation(self, *args, **kwargs):
        raise NotImplementedError(
            "'/user/resend_confirmation' call is depricated and is not supported by "
            "this app")

    def account(self, account_id, **kwargs):
        allowed_params = ['account_id']
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/account', params=params, allowed_params=allowed_params)

    def account_find(self, **kwargs):
        allowed_params = ['name', 'reference_id', 'sort_order']
        return self.make_call(
            '/account/find', params=kwargs, allowed_params=allowed_params)

    def account_create(self, name, description, **kwargs):
        allowed_params = [
            'name', 'description', 'reference_id', 'type', 'image_uri',
            'gaq_domains', 'theme_object', 'mcc', 'callback_uri'
        ]
        params = {
            'name': name,
            'description': description
        }
        params.update(kwargs)
        return self.make_call(
            '/account/create', params=params, allowed_params=allowed_params)

    def account_modify(self, account_id, **kwargs):
        allowed_params = [
            'account_id', 'name', 'description', 'reference_id', 'image_uri', 
            'gaq_domains', 'theme_object', 'callback_uri'
        ]
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/account/modify', params=params, allowed_params=allowed_params)

    def account_delete(self, account_id, **kwargs):
        allowed_params = ['account_id', 'reason']
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/account/delete', params=params, allowed_params=allowed_params)

    def account_balance(self, account_id, **kwargs):
        allowed_params = ['account_id']
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/account/balance', params, allowed_params=allowed_params)
        
    def account_add_bank(self, account_id, **kwargs):
        allowed_params = ['account_id', 'mode', 'redirect_uri']
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/account/add_bank', params=params, allowed_params=allowed_params)
        
    def account_set_tax(self, account_id, taxes, **kwargs):
        allowed_params = ['account_id', 'taxes']
        params = {
            'account_id': account_id,
            'taxes': taxes
        }
        params.update(kwargs)
        return self.make_call(
            '/account/set_tax', params=params, allowed_params=allowed_params)

    def account_get_tax(self, account_id, **kwargs):
        allowed_params = ['account_id']
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/account/get_tax', params=params, allowed_params=allowed_params)

    def checkout(self, checkout_id, **kwargs):
        allowed_params = ['checkout_id']
        params = {
            'checkout_id': checkout_id
        }
        params.update(kwargs)
        return self.make_call(
            '/checkout', params=params, allowed_params=allowed_params)

    def checkout_find(self, account_id, **kwargs):
        allowed_params = [
            'account_id', 'start', 'limit', 'reference_id', 'state', 
            'preapproval_id', 'start_time', 'end_time', 'sort_order', 'shipping_fee'
        ]
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/checkout/find', params=params, allowed_params=allowed_params)

    def checkout_create(self, account_id, short_description, type, amount, **kwargs):
        # decide on type, payer_email_message, payee_email_message, fallback_uri,
        # shipping fee, charge_tax, prefill_info, funding_sources, payment_method_id,
        # payment_method_type
        # to save in db or not
        allowed_params = [
            'account_id', 'short_description', 'type', 'amount', 'long_description', 
            'payer_email_message', 'payee_email_message', 'reference_id', 'app_fee',
            'fee_payer', 'redirect_uri', 'callback_uri', 'fallback_uri', 
            'auto_capture', 'require_shipping', 'shipping_fee', 'charge_tax', 'mode',
            'preapproval_id', 'prefill_info', 'funding_sources', 'payment_method_id',
            'payment_method_type'
        ]
        params = {
            'account_id': account_id,
            'short_description': short_description,
            'type': type,
            'amount': amount
        }
        params.update(kwargs)
        return self.make_call(
            '/checkout/create', params=params, allowed_params=allowed_params)

    def checkout_cancel(self, checkout_id, **kwargs):
        allowed_params = ['checkout_id', 'cancel_reason']
        params = {
            'checkout_id': checkout_id
        }
        params.update(kwargs)
        return self.make_call(
            '/checkout/cancel', params=params, allowed_params=allowed_params)

    def checkout_refund(self, checkout_id, **kwargs):
        allowed_params = [
            'checkout_id', 'refund_reason', 'amount', 'app_fee',
            'payer_email_message', 'payee_email_message'
        ]
        params = {
            'checkout_id': checkout_id
        }
        params.update(kwargs)
        return self.make_call(
            '/checkout/refund', params=params, allowed_params=allowed_params)

    def checkout_capture(self, checkout_id, **kwargs):
        allowed_params = ['checkout_id']
        params = {
            'checkout_id': checkout_id
        }
        params.update(kwargs)
        return self.make_call(
            '/checkout/capture', params=params, allowed_params=allowed_params)

    def checkout_modify(self, checkout_id, **kwargs):
        allowed_params = ['checkout_id', 'callback_uri']
        params = {
            'checkout_id': checkout_id
        }
        params.update(kwargs)
        return self.make_call(
            '/checkout/modify', params=params, allowed_params=allowed_params)


    def preapproval(self, preapproval_id, **kwargs):
        allowed_params = ['preapproval_id']
        params = {
            'preapproval_id': preapproval_id
        }
        params.update(kwargs)
        return self.make_call(
            '/preapproval', params=params, allowed_params=allowed_params)

    def preapproval_find(self, **kwargs):
        allowed_params = [
            'account_id', 'state', 'reference_id', 'start', 'limit', 'sort_order', 
            'last_checkout_id', 'shipping_fee'
        ]
        return self.make_call(
            '/preapproval/find', params=kwargs, allowed_params=allowed_params)

    def preapproval_create(self, short_description, period, **kwargs):
        allowed_params = [
            'account_id', 'amount', 'short_description', 'period', 'reference_id', 
            'app_fee', 'fee_payer', 'redirect_uri', 'callback_uri', 'fallback_uri', 
            'require_shipping', 'shipping_fee', 'charge_tax', 'payer_email_message',
            'long_description', 'frequency', 'start_time','end_time', 'auto_recur',
            'mode', 'prefill_info', 'funding_sources', 'payment_method_id',
            'payment_method_type'
        ]
        params = {
            'short_description': short_description,
            'period': period
        }
        params.update(kwargs)
        return self.make_call(
            '/preapproval/create', params=params, allowed_params=allowed_params)

    def preapproval_cancel(self, preapproval_id, **kwargs):
        allowed_params = ['preapproval_id']
        params = {
            'preapproval_id': preapproval_id
        }
        params.update(kwargs)
        return self.make_call(
            '/preapproval/cancel', params=params, allowed_params=allowed_params)

    def preapproval_modify(self, preapproval_id, **kwargs):
        allowed_params = ['preapproval_id', 'callback_uri']
        params = {
            'preapproval_id': preapproval_id
        }
        params.update(kwargs)
        return self.make_call(
            '/preapproval/modify', params=params, allowed_params=allowed_params)

    def withdrawal(self, withdrawal_id, **kwargs):
        allowed_params = ['withdrawal_id']
        params = {
            'withdrawal_id': withdrawal_id
        }
        params.update(kwargs)
        return self.make_call(
            '/withdrawal', params=params, allowed_params=allowed_params)

    def withdrawal_find(self, account_id, **kwargs):
        allowed_params = ['account_id', 'limit', 'start', 'sort_order']
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/withdrawal/find', params=params, allowed_params=allowed_params)

    def withdrawal_create(self, account_id, **kwargs):
        allowed_params = [
            'account_id', 'redirect_uri', 'callback_uri', 'note', 'mode'
        ]
        params = {
            'account_id': account_id
        }
        params.update(kwargs)
        return self.make_call(
            '/withdrawal/create', params=params, allowed_params=allowed_params)

    def withdrawal_modify(self, withdrawal_id, **kwargs):
        allowed_params = ['withdrawal_id', 'callback_uri']
        params = {
            'withdrawal_id': withdrawal_id
        }
        params.update(kwargs)
        return self.make_call(
            '/withdrawal/modify', params=params, allowed_params=allowed_params)


    def credit_card(self, client_id, client_secret, credit_card_id, **kwargs):
        allowed_params = ['client_id', 'client_secret', 'credit_card_id']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        params.update(kwargs)
        return self.make_call(
            '/credit_card', params=params, allowed_params=allowed_params)

    def credit_card_create(self, client_id, cc_number, cvv, expiration_month, 
                          expiration_year, user_name, email, address, **kwargs):
        allowed_params = [
            'client_id', 'cc_number', 'cvv', 'expiration_month', 'expiration_year',
            'user_name', 'email', 'address'
        ]
        params = {
            'client_id': client_id,
            'cc_number': cc_number, 
            'cvv': cvv,
            'expiration_month': expiration_month,
            'expiration_year': expiration_year,
            'user_name': user_name,
            'email': email,
            'address': address
        }
        params.update(kwargs)
        return self.make_call(
            '/credit_card/create', params=params, allowed_params=allowed_params)

    def credit_card_authorize(self, client_id, client_secret, credit_card_id, 
                             **kwargs):
        allowed_params = ['client_id', 'client_secret', 'credit_card_id']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        params.update(kwargs)
        return self.make_call(
            '/credit_card/autorize', params=params, allowed_params=allowed_params)

    def credit_card_find(self, client_id, client_secret, **kwargs):
        allowed_params = [
            'client_id', 'client_secret', 'reference_id', 'limit', 'start', 
            'sort_order'
        ]
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        params.update(kwargs)
        return self.make_call(
            '/credit_card/find', params=params, allowed_params=allowed_params)

    def credit_card_delete(self, client_id, client_secret, credit_card_id, **kwargs):
        allowed_params = ['client_id', 'client_secret', 'credit_card_id']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        params.update(kwargs)
        return self.make_call(
            '/credit_card/delete', params=params, allowed_params=allowed_params)

    def batch_create(self, client_id, client_secret, calls, **kwargs):
        allowed_params = ['client_id', 'client_secret', 'calls']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'calls': calls
        }
        params.update(kwargs)
        return self.make_call(
            '/batch/create', params=params, allowed_params=allowed_params)

