"""This module was designed to help making `WePay <https://wepay.com>`_ API calls. 

.. moduleauthor:: lehins <lehins@yandex.ru>
   :platform: independent
"""
import urllib, urllib2, json, warnings

from wepay.exceptions import WePayError

__all__ = ["WePay"]


class WePay(object):
    """A full client for the WePay API. """

    floating = ['amount', 'app_fee', 'shipping_fee', 'setup_fee']

    class WePayWarning(UserWarning):
        pass
    
    def __init__(self, production=True, access_token=None, timeout=30):
        """The main class for making calls

        :keyword bool production: When ``False``, the ``stage.wepay.com`` API
            server will be used instead of the default production.
        :keyword str access_token: The access token associated with your
            application.
        :keyword int timeout: time in seconds before HTTPS call request will timeout
        """
        self.production = production
        self.access_token = access_token
        self._timeout = timeout
        if production:
            self.api_endpoint = "https://wepayapi.com/v2"
            self.browser_uri = "https://www.wepay.com"
            self.browser_js = self.browser_uri + "/min/js/wepay.v2.js"
            self.browser_iframe_js = self.browser_uri + "/min/js/iframe.wepay.js"
        else:
            self.api_endpoint = "https://stage.wepayapi.com/v2"
            self.browser_uri = "https://stage.wepay.com"
            self.browser_js = self.browser_uri + "/js/wepay.v2.js"
            self.browser_iframe_js = self.browser_uri + "/js/iframe.wepay.js"
        self.browser_endpoint = self.browser_uri + "/v2"
    

    def _update_params(self, params, kwargs, 
                       keywords=['access_token', 'batch_mode']):
        optional_kwargs = {}
        for key in keywords:
            if key in kwargs:
                optional_kwargs[key] = kwargs.pop(key)
        params.update(kwargs)
        return optional_kwargs

    def call(self, uri, params=None, access_token=None, token=None):
        """Calls wepay.com/v2/``uri`` with ``params`` and returns the JSON response as a
        python dict. The optional ``access_token`` parameter will override the
        instance's ``access_token`` if it is set. Basically the same call
        function as in Python-SDK WePay API with a minor change, header was
        changed to 'Python WePay SDK (third party)'.  Essentially this is the
        place for all api calls.

        :param str uri: API uri to call
        :keyword dict params: parameters to include in the call
        :keyword str access_token: access_token to use for the call.
        :keyword str token: only here for compatibility with official Python WePay 
            SDK. Use ``access_token`` instead.
        :returns: dict -- WePay response as documented per call
        :raises: :mod:`wepay.exceptions.WePayError`

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
            
        if not params is None:
            params = json.dumps(params)

        request = urllib2.Request(url, params, headers)
        try:
            response = urllib2.urlopen(request, timeout=self._timeout).read()
            return json.loads(response)
        except urllib2.HTTPError as e:
            response = json.loads(e.read())
            raise WePayError(response['error'], response['error_description'], 
                             response['error_code'])
       
    def get_authorization_url(self, redirect_uri, client_id, options=None,
                              scope=None):
        """Returns a URL to send the user to in order to get authorization.  After
        getting authorization the user will return to redirect_uri.  Optionally,
        scope can be set to limit permissions, and the options dict can be
        loaded with any combination of state, user_name or user_email.

        .. note::

           This function is here for compatibilty with official Python WePay SDK 
           only, use :func:`oauth2_authorize` instead.           
        
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
        """Calls wepay.com/v2/oauth2/token to get an access token. Sets the
        access_token for the WePay instance and returns the entire response as a
        dict. Should only be called after the user returns from being sent to
        get_authorization_url.

        .. note::

           This function is here for compatibilty with official Python WePay SDK
           only, use :func:`oauth2_token` instead.

        :param str redirect_uri: The same URI specified in the
            :py:meth:`get_authorization_url` call that preceeded this.
        :param str client_id: The client ID issued by WePay to your app.
        :param str client_secret: The client secret issued by WePay
            to your app.
        :param str code: The code returned by :py:meth:`get_authorization_url`.

        """
        warnings.warn("'get_token' is deprecated and is here only "
                      "for compatibility with official Python WePay SDK. "
                      "Use 'WePay.oauth2_token' instead.", DeprecationWarning)
        response = self.oauth2_token(*args, **kwargs)
        self.access_token = response['access_token']
        return response

    def make_call(self, uri, params={}, allowed_params=[], access_token=None,
                  batch_mode=False):
        """This is a helper function that checks the validity of ``params`` dictionary
        by matching it with ``allowed_params`` and then performs a call.  Will
        issue a `WePayWarning` in case of unrecognized parameter, and raise a
        `WePayError` after making a call, in case if it is in fact unrecognized.
        If ``batch_mode`` is set to ``True`` instead of making a call it will
        construct a dictionary that is ready to be used in :func:`batch_create`
        later on, while ``refernce_id`` can also be added to it later, as
        specified by WePay Documentation, see :func:`batch_create`.

        :param str uri: API uri to call
        :keyword dict params: parameters to include in the call
        :keyword list allowed_params: list of names of allowed params
        :keyword str access_token: access_token to use for the call.
        :keyword bool batch_mode: perform a call or construct a batch call
        :returns: dict -- depending on ``batch_mode`` flag, either WePay response 
            through calling :func:`call` or a dictionary that is ready 
            to be appended to ``calls`` list that is passed to :func:`batch_create`
        :raises: :mod:`wepay.exceptions.WePayError`

        """
        unrecognized_params = set(params) - set(allowed_params)
        if unrecognized_params:
            warnings.warn(
                "At least one of the parameters to the api call: '%s' is "
                "unrecognized. Allowed parameters are: '%s'. Unrecognized "
                "parameters are: '%s'." % 
                (uri, ', '.join(allowed_params), ', '.join(unrecognized_params)), 
                self.WePayWarning)
        for name in self.floating:
            if name in params:
                params[name] = float(params[name])
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
        """Call documentation: `/oauth2/authorize
        <https://www.wepay.com/developer/reference/oauth2#authorize>`_.

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
        """Call documentation: `/oauth2/token
        <https://www.wepay.com/developer/reference/oauth2#token>`_, plus extra
        keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

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
        return self.make_call(
            '/oauth2/token', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def app(self, client_id, client_secret, **kwargs):
        """Call documentation: `/app
        <https://www.wepay.com/developer/reference/app#lookup>`_, plus extra
        keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['client_id', 'client_secret']
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        return self.make_call(
            '/app', params=params, allowed_params=allowed_params, 
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def app_modify(self, client_id, client_secret, **kwargs):
        """Call documentation: `/app/modify
        <https://www.wepay.com/developer/reference/app#modify>`_, plus extra
        keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'client_id', 'client_secret', 'theme_object', 'gaq_domains'
        ]
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        return self.make_call(
            '/app/modify', params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def user(self, **kwargs):
        """Call documentation: `/user
        <https://www.wepay.com/developer/reference/user#lookup>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        params = {}
        return self.make_call('/user', params=params,
                              **self._update_params(params, kwargs))

    def user_modify(self, **kwargs):
        """Call documentation: `/user/modify
        <https://www.wepay.com/developer/reference/user#modify>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['callback_uri']
        params = {}
        return self.make_call(
            '/user/modify', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def user_register(self, *args, **kwargs):
        """Call documentation: `/user/register
        <https://www.wepay.com/developer/reference/user#register>`_.

        :raises: `NotImplementedError`

        .. warning ::

            This API call is depricated, therefore is not implemented.

        """
        raise NotImplementedError(
            "'/user/register' call is depricated and is not supported by this app")

    def user_resend_confirmation(self, *args, **kwargs):
        """Call documentation: `/user/resend_confirmation
        <https://www.wepay.com/developer/reference/user#resend_confirmation>`_.

        :raises: `NotImplementedError`

        .. warning ::

            This API call is depricated, therefore is not implemented.

        """
        raise NotImplementedError(
            "'/user/resend_confirmation' call is depricated and is not supported by "
            "this app")

    def account(self, account_id, **kwargs):
        """Call documentation: `/account
        <https://www.wepay.com/developer/reference/account#lookup>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id']
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/account', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def account_find(self, **kwargs):
        """Call documentation: `/account/find
        <https://www.wepay.com/developer/reference/account#find>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['name', 'reference_id', 'sort_order']
        params = {}
        return self.make_call(
            '/account/find', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def account_create(self, name, description, **kwargs):
        """Call documentation: `/account/create
        <https://www.wepay.com/developer/reference/account#create>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'name', 'description', 'reference_id', 'type', 'image_uri',
            'gaq_domains', 'theme_object', 'mcc', 'callback_uri'
        ]
        params = {
            'name': name,
            'description': description
        }
        return self.make_call(
            '/account/create', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def account_modify(self, account_id, **kwargs):
        """Call documentation: `/account/modify
        <https://www.wepay.com/developer/reference/account#modify>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'account_id', 'name', 'description', 'reference_id', 'image_uri', 
            'gaq_domains', 'theme_object', 'callback_uri'
        ]
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/account/modify', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def account_delete(self, account_id, **kwargs):
        """Call documentation: `/account/delete
        <https://www.wepay.com/developer/reference/account#delete>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id', 'reason']
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/account/delete', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def account_balance(self, account_id, **kwargs):
        """Call documentation: `/account/balance
        <https://www.wepay.com/developer/reference/account#balance>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id']
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/account/balance', params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))
        
    def account_add_bank(self, account_id, **kwargs):
        """Call documentation: `/account/add_bank
        <https://www.wepay.com/developer/reference/account#add_bank>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id', 'mode', 'redirect_uri']
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/account/add_bank', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))
        
    def account_set_tax(self, account_id, taxes, **kwargs):
        """Call documentation: `/account/set_tax
        <https://www.wepay.com/developer/reference/account#set_tax>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id', 'taxes']
        params = {
            'account_id': account_id,
            'taxes': taxes
        }
        return self.make_call(
            '/account/set_tax', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def account_get_tax(self, account_id, **kwargs):
        """Call documentation: `/account/get_tax
        <https://www.wepay.com/developer/reference/account#get_tax>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id']
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/account/get_tax', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def checkout(self, checkout_id, **kwargs):
        """Call documentation: `/checkout
        <https://www.wepay.com/developer/reference/checkout#lookup>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['checkout_id']
        params = {
            'checkout_id': checkout_id
        }
        return self.make_call(
            '/checkout', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def checkout_find(self, account_id, **kwargs):
        """Call documentation: `/checkout/find
        <https://www.wepay.com/developer/reference/checkout#find>`_, plus extra
        keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'account_id', 'start', 'limit', 'reference_id', 'state', 
            'preapproval_id', 'start_time', 'end_time', 'sort_order', 'shipping_fee'
        ]
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/checkout/find', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def checkout_create(self, account_id, short_description, type, amount, **kwargs):
        """Call documentation: `/checkout/create
        <https://www.wepay.com/developer/reference/checkout#create>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
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
        return self.make_call(
            '/checkout/create', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def checkout_cancel(self, checkout_id, cancel_reason, **kwargs):
        """Call documentation: `/checkout/cancel
        <https://www.wepay.com/developer/reference/checkout#cancel>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['checkout_id', 'cancel_reason']
        params = {
            'checkout_id': checkout_id,
            'cancel_reason': cancel_reason
        }
        return self.make_call(
            '/checkout/cancel', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def checkout_refund(self, checkout_id, refund_reason, **kwargs):
        """Call documentation: `/checkout/refund
        <https://www.wepay.com/developer/reference/checkout#refund>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'checkout_id', 'refund_reason', 'amount', 'app_fee',
            'payer_email_message', 'payee_email_message'
        ]
        params = {
            'checkout_id': checkout_id,
            'refund_reason': refund_reason
        }
        return self.make_call(
            '/checkout/refund', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def checkout_capture(self, checkout_id, **kwargs):
        """Call documentation: `/checkout/capture
        <https://www.wepay.com/developer/reference/checkout#capture>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['checkout_id']
        params = {
            'checkout_id': checkout_id
        }
        return self.make_call(
            '/checkout/capture', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def checkout_modify(self, checkout_id, **kwargs):
        """Call documentation: `/checkout/modify
        <https://www.wepay.com/developer/reference/checkout#modify>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['checkout_id', 'callback_uri']
        params = {
            'checkout_id': checkout_id
        }
        return self.make_call(
            '/checkout/modify', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))


    def preapproval(self, preapproval_id, **kwargs):
        """Call documentation: `/preapproval
        <https://www.wepay.com/developer/reference/preapproval#lookup>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['preapproval_id']
        params = {
            'preapproval_id': preapproval_id
        }
        return self.make_call(
            '/preapproval', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def preapproval_find(self, **kwargs):
        """Call documentation: `/preapproval/find
        <https://www.wepay.com/developer/reference/preapproval#find>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'account_id', 'state', 'reference_id', 'start', 'limit', 'sort_order', 
            'last_checkout_id', 'shipping_fee'
        ]
        params = {}
        return self.make_call(
            '/preapproval/find', params=kwargs, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def preapproval_create(self, short_description, period, **kwargs):
        """Call documentation: `/preapproval/create
        <https://www.wepay.com/developer/reference/preapproval#create>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'account_id', 'amount', 'short_description', 'period', 'reference_id', 
            'app_fee', 'fee_payer', 'redirect_uri', 'callback_uri', 'fallback_uri', 
            'require_shipping', 'shipping_fee', 'charge_tax', 'payer_email_message',
            'long_description', 'frequency', 'start_time','end_time', 'auto_recur',
            'mode', 'prefill_info', 'funding_sources', 'payment_method_id',
            'payment_method_type', 'client_id', 'client_secret'
        ]
        params = {
            'short_description': short_description,
            'period': period
        }
        return self.make_call(
            '/preapproval/create', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def preapproval_cancel(self, preapproval_id, **kwargs):
        """Call documentation: `/preapproval/cancel
        <https://www.wepay.com/developer/reference/preapproval#cancel>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['preapproval_id']
        params = {
            'preapproval_id': preapproval_id
        }
        return self.make_call(
            '/preapproval/cancel', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def preapproval_modify(self, preapproval_id, **kwargs):
        """Call documentation: `/preapproval/modify
        <https://www.wepay.com/developer/reference/preapproval#modify>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['preapproval_id', 'callback_uri']
        params = {
            'preapproval_id': preapproval_id
        }
        return self.make_call(
            '/preapproval/modify', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def withdrawal(self, withdrawal_id, **kwargs):
        """Call documentation: `/withdrawal
        <https://www.wepay.com/developer/reference/withdrawal#lookup>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['withdrawal_id']
        params = {
            'withdrawal_id': withdrawal_id
        }
        return self.make_call(
            '/withdrawal', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def withdrawal_find(self, account_id, **kwargs):
        """Call documentation: `/withdrawal/find
        <https://www.wepay.com/developer/reference/withdrawal#find>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id', 'limit', 'start', 'sort_order']
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/withdrawal/find', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def withdrawal_create(self, account_id, **kwargs):
        """Call documentation: `/withdrawal/create
        <https://www.wepay.com/developer/reference/withdrawal#create>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'account_id', 'redirect_uri', 'callback_uri', 'fallback_uri', 'note', 
            'mode'            
        ]
        params = {
            'account_id': account_id
        }
        return self.make_call(
            '/withdrawal/create', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def withdrawal_modify(self, withdrawal_id, **kwargs):
        """Call documentation: `/withdrawal/modify
        <https://www.wepay.com/developer/reference/withdrawal#modify>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['withdrawal_id', 'callback_uri']
        params = {
            'withdrawal_id': withdrawal_id
        }
        return self.make_call(
            '/withdrawal/modify', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))


    def credit_card(self, client_id, client_secret, credit_card_id, **kwargs):
        """Call documentation: `/credit_card
        <https://www.wepay.com/developer/reference/credit_card#lookup>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['client_id', 'client_secret', 'credit_card_id']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        return self.make_call(
            '/credit_card', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def credit_card_create(self, client_id, cc_number, cvv, expiration_month, 
                           expiration_year, user_name, email, address, 
                           original_ip, original_device, **kwargs):
        """Call documentation: `/credit_card/create
        <https://www.wepay.com/developer/reference/credit_card#create>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'client_id', 'cc_number', 'cvv', 'expiration_month', 'expiration_year',
            'user_name', 'email', 'address', 'original_ip', 'original_device'
        ]
        params = {
            'client_id': client_id,
            'cc_number': cc_number, 
            'cvv': cvv,
            'expiration_month': expiration_month,
            'expiration_year': expiration_year,
            'user_name': user_name,
            'email': email,
            'address': address,
            'original_ip': original_ip,
            'original_device': original_device
        }
        return self.make_call(
            '/credit_card/create', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def credit_card_authorize(self, client_id, client_secret, credit_card_id, 
                              **kwargs):
        """Call documentation: `/credit_card/authorize
        <https://www.wepay.com/developer/reference/credit_card#authorize>`_,
        plus extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['client_id', 'client_secret', 'credit_card_id']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        return self.make_call(
            '/credit_card/authorize', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def credit_card_find(self, client_id, client_secret, **kwargs):
        """Call documentation: `/credit_card/find
        <https://www.wepay.com/developer/reference/credit_card#find>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'client_id', 'client_secret', 'reference_id', 'limit', 'start', 
            'sort_order'
        ]
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        return self.make_call(
            '/credit_card/find', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def credit_card_delete(self, client_id, client_secret, credit_card_id, **kwargs):
        """Call documentation: `/credit_card/delete
        <https://www.wepay.com/developer/reference/credit_card#delete>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['client_id', 'client_secret', 'credit_card_id']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        return self.make_call(
            '/credit_card/delete', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['batch_mode']))

    def subscription_plan(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription_plan
        <https://www.wepay.com/developer/reference/subscription_plan#lookup>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['subscription_plan_id']
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(
            '/subscription_plan', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def subscription_plan_find(self, **kwargs):
        """Call documentation: `/subscription_plan/find
        <https://www.wepay.com/developer/reference/subscription_plan#find>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['account_id', 'start', 'limit', 'state', 'reference_id']
        params = {}
        return self.make_call(
            '/subscription_plan/find', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def subscription_plan_create(self, account_id, name, short_description,
                                 amount, period, **kwargs):
        """Call documentation: `/subscription_plan/create
        <https://www.wepay.com/developer/reference/subscription_plan#create>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'account_id', 'name', 'short_description', 'amount', 'period', 
            'app_fee', 'callback_uri', 'trial_length', 'setup_fee', 'reference_id'
        ]
        params = {
            'account_id': account_id,
            'name': name,
            'short_description': short_description,
            'amount': amount,
            'period': period
        }
        return self.make_call(
            '/subscription_plan/create', params=params, 
            allowed_params=allowed_params, **self._update_params(params, kwargs))

    def subscription_plan_delete(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription_plan/delete
        <https://www.wepay.com/developer/reference/subscription_plan#delete>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['subscription_plan_id', 'reason']
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(
            '/subscription_plan/delete', params=params, 
            allowed_params=allowed_params, **self._update_params(params, kwargs))

    def subscription_plan_get_button(self, account_id, button_type, **kwargs):
        """Call documentation: `/subscription_plan/get_button
        <https://www.wepay.com/developer/reference/subscription_plan#get_button>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'account_id', 'button_type', 'subscription_plan_id', 'button_text',
            'button_options'
        ]
        params = {
            'account_id': account_id,
            'button_type': button_type
        }
        return self.make_call(
            '/subscription_plan/get_button', params=params, 
            allowed_params=allowed_params, **self._update_params(params, kwargs))

    def subscription_plan_modify(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription_plan/modify
        <https://www.wepay.com/developer/reference/subscription_plan#modify>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'subscription_plan_id', 'name', 'short_description', 'amount', 
            'app_fee', 'callback_uri', 'trial_length', 'setup_fee', 
            'update_subscriptions', 'transition_expire_days', 'reference_id'
        ]
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(
            '/subscription_plan/modify', params=params, 
            allowed_params=allowed_params, **self._update_params(params, kwargs))


    def subscription(self, subscription_id, **kwargs):
        """Call documentation: `/subscription
        <https://www.wepay.com/developer/reference/subscription#lookup>`_, plus
        extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['subscription_id']
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(
            '/subscription', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))


    def subscription_find(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription/find
        <https://www.wepay.com/developer/reference/subscription#find>`_, plus
        extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'subscription_plan_id', 'start', 'limit', 'start_time', 'end_time',
            'state', 'reference_id'
        ]
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(
            '/subscription/find', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))
        
        
    def subscription_create(self, subscription_plan_id, redirect_uri, **kwargs):
        """Call documentation: `/subscription/create
        <https://www.wepay.com/developer/reference/subscription#create>`_, plus
        extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'subscription_plan_id', 'redirect_uri', 'callback_uri', 
            'payment_method_id', 'payment_method_type', 'mode', 'quantity',
            'reference_id', 'prefill_info'
        ]
        params = {
            'subscription_plan_id': subscription_plan_id,
            'redirect_uri': redirect_uri
        }
        return self.make_call(
            '/subscription/create', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def subscription_cancel(self, subscription_id, **kwargs):
        """Call documentation: `/subscription/cancel
        <https://www.wepay.com/developer/reference/subscription#cancel>`_, plus
        extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['subscription_id', 'reason']
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(
            '/subscription/cancel', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def subscription_modify(self, subscription_id, **kwargs):
        """Call documentation: `/subscription/modify
        <https://www.wepay.com/developer/reference/subscription#modify>`_, plus
        extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'subscription_id', 'redirect_uri', 'callback_uri', 
            'payment_method_id', 'payment_method_type', 'quantity', 'reference_id',
            'transition_expire_days', 'extend_trial_days', 'prorate'
        ]
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(
            '/subscription/modify', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs))

    def subscription_charge(self, subscription_charge_id, **kwargs):
        """Call documentation: `/subscription_charge
        <https://www.wepay.com/developer/reference/subscription_charge#lookup>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['subscription_charge_id']
        params = {
            'subscription_charge_id': subscription_charge_id
        }
        return self.make_call(
            '/subscription_charge', params=params, 
            allowed_params=allowed_params, **self._update_params(params, kwargs))

    def subscription_charge_find(self, subscription_id, **kwargs):
        """Call documentation: `/subscription_charge/find
        <https://www.wepay.com/developer/reference/subscription_charge#find>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = [
            'subscription_id', 'start', 'limit', 'start_time', 'end_time',
            'type', 'state'
        ]
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(
            '/subscription_charge/find', params=params, 
            allowed_params=allowed_params, **self._update_params(params, kwargs))

    def subscription_charge_refund(self, subscription_charge_id, **kwargs):
        """Call documentation: `/subscription_charge/refund
        <https://www.wepay.com/developer/reference/subscription_charge#refund>`_,
        plus extra keyword parameters:
        
        .. note::

           This Api call is in beta mode at WePay. Moreover it is also in beta
           mode in this SDK and it hasn't been tested. In case if you spot any
           bugs or have suggestions, please, open an issue on `github
           <https://github.com/lehins/python-wepay>`_ or send me an email to
           lehins@ya.ru

        :keyword str access_token: will be used instead of instance's
            ``access_token``
        :keyword bool batch_mode: turn on/off the batch_mode, see :func:`make_call`

        """
        allowed_params = ['subscription_charge_id', 'refund_reason']
        params = {
            'subscription_charge_id': subscription_charge_id
        }
        return self.make_call(
            '/subscription_charge/refund', params=params, 
            allowed_params=allowed_params, **self._update_params(params, kwargs))


    def batch_create(self, client_id, client_secret, calls, **kwargs):
        """Call documentation: `/batch/create
        <https://www.wepay.com/developer/reference/batch#create>`_, plus extra
        keyword parameter:
        
        :keyword str access_token: will be used instead of instance's
            ``access_token``

        """
        allowed_params = ['client_id', 'client_secret', 'calls']
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'calls': calls
        }
        return self.make_call(
            '/batch/create', params=params, allowed_params=allowed_params,
            **self._update_params(params, kwargs, keywords=['access_token']))

