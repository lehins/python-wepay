"""This module was designed to help making `WePay <https://wepay.com>`_ API calls. 

.. moduleauthor:: lehins <lehins@yandex.ru>
   :platform: independent
"""
import warnings

from wepay.calls import *
from wepay.utils import Post

__all__ = ['WePay']


class WePay(object):
    """A full client for the WePay API.
    
    :keyword bool production: When ``False``, the ``stage.wepay.com`` API
       server will be used instead of the default production.
    :keyword str access_token: The access token associated with your
       application.
    :keyword str api_version: sets default version of API which will be
       accepting calls. It is also possible to specify different version
       per API call, since all calls accept a keyword argument
       `api_version` as well. `More on API versioning
       <https://stage.wepay.com/developer/tutorial/versioning>`_.
    :keyword float timeout: time in seconds before HTTPS call request will timeout.
       Also can be changed on per call basis.
    :keyword bool silent: if set to `None` (default) will print
       :exc:`WePayWarning<wepay.exceptions.WePayWarning>` if `production=True` and
       raise them otherwise. Set it to `True` to stop parameter validation and
       suppress all warnings, or `False` to raise all warnings.

    :keyword bool use_requests: set to `False` in order to explicitly turn off
       `requests <http://docs.python-requests.org/en/latest/>`_ library usage and
       fallback to `urllib <https://docs.python.org/3/library/urllib.html#module-urllib>`_

    Instance of this class contains attributes, which correspond to WePay
    objects and should be used to perform API calls. If a WePay object has a
    lookup call, corresponding attribute will also be callable. Example:

        >>> api = WePay(production=False, access_token=WEPAY_ACCESS_TOKEN)
        >>> response = api.account.create('Test Account', 'Short Description')
        >>> api.account(response['account_id'])

    Each method that performs an API call accepts all required parameters as
    positional arguments, optional parameters as keyword arguments, as well as
    one or more keyword arguments that are used to control behavior of a
    call. All these methods accept keyword arguments ``api_version``,
    ``timeout`` and if documented also possible keyword arguments
    ``batch_mode``, ``batch_reference_id`` and ``access_token``:

       * ``api_version`` will make sure the call is made to a specified API version
         (cannot be used together with ``batch_mode``)

       * ``timeout`` specifies a connection timeout in seconds for the call
         (cannot be used together with ``batch_mode``)

       * ``access_token`` will make sure the call is made with this
         access_token, also use it to set `authorization` param in
         ``batch_mode``.

       * ``batch_mode`` instead of performing an actual call to WePay, a method
         will return a dictionary that is ready to be added to `/batch/create`,
         namely to calls list parameter. :meth:`batch.create<wepay.calls.batch.Batch.create>`

       * ``batch_reference_id`` will set `reference_id` param in a batch call,
         it is an error to use it without ``batch_mode`` set to ``True``

    Batch mode usage example:
        >>> api = WePay(production=False, access_token=WEPAY_ACCESS_TOKEN)
        >>> calls = []
        >>> calls.append(api.account.create('Test Account', 'Short Description', batch_mode=True, access_token='STAGE_...', batch_reference_id='c1'))
        >>> calls.append(api.checkout(12345, batch_mode=True))
        >>> api.batch.create(CLIENT_ID, CLIENT_SECRET, calls)

    API Call objects:

    .. attribute:: oauth2 =
   
       :class:`OAuth2<wepay.calls.oauth2.OAuth2>` call instance
 
    .. attribute:: app =
   
       :class:`App<wepay.calls.app.App>` call instance

    .. attribute:: user =
   
       :class:`User<wepay.calls.user.User>` call instance

    .. attribute:: account =
   
       :class:`Account<wepay.calls.account.Account>` call instance

    .. attribute:: checkout =
   
       :class:`Checkout<wepay.calls.checkout.Checkout>` call instance

    .. attribute:: preapproval =
   
       :class:`Preapproval<wepay.calls.preapproval.Preapproval>` call instance

    .. attribute:: withdrawal =
   
       :class:`Withdrawal<wepay.calls.withdrawal.Withdrawal>` call instance

    .. attribute:: credit_card =
   
       :class:`CreditCard<wepay.calls.credit_card.CreditCard>` call instance

    .. attribute:: subscription_plan =
   
       :class:`SubscriptionPlan<wepay.calls.subscription_plan.SubscriptionPlan>` call instance

    .. attribute:: subscription =
   
       :class:`Subscription<wepay.calls.subscription.Subscription>` call instance

    .. attribute:: subscription_charge =
   
       :class:`SubscriptionCharge<wepay.calls.subscription_charge.SubscriptionCharge>`
       call instance

    .. attribute:: batch =
   
       :class:`Batch<wepay.calls.batch.Batch>` call instance

    """

    supported_calls = [
        OAuth2, App, User, Account, Checkout, Preapproval, Withdrawal, CreditCard,
        SubscriptionPlan, Subscription, SubscriptionCharge, Batch
    ]
    """List of supported objects. Override this list in case custom behavior is
    required (for instance supplying default values to a particular call or
    turning off support for certain objects)

    """

    def __init__(self, production=True, access_token=None, api_version=None,
                 timeout=30, silent=None, use_requests=None):
        self.production = production
        self.access_token = access_token
        self.api_version = api_version
        self.silent = silent
        self._timeout = timeout
        self._post = Post(use_requests=use_requests, silent=silent)
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
        for call_cls in self.supported_calls:
            setattr(self, call_cls.call_name, call_cls(self))
        self._backwards()
    
    def call(self, uri, params=None, access_token=None, api_version=None, timeout=None,
             token=None):

        """Calls wepay.com/v2/``uri`` with ``params`` and returns the JSON
        response as a python `dict`. The optional ``access_token`` parameter
        takes precedence over instance's ``access_token`` if it is
        set. Essentially this is the place for all api calls.

        :param str uri: API uri to call
        :keyword dict params: parameters to include in the call
        :keyword str access_token: access_token to use for the call.
        :keyword str api_version: allows to create a call to specific version of API
        :keyword float timeout: a way to specify a call timeout in seconds. If `None`
            will use `WePay.timeout`.
        :keyword str token: only here for compatibility with official Python WePay 
            SDK. Use ``access_token`` instead.
        :return: WePay response as documented per call
        :rtype: dict
        :raises: :exc:`WePayClientError<wepay.exceptions.WePayClientError>`
        :raises: :exc:`WePayServerError<wepay.exceptions.WePayServerError>`
        :raises: :exc:`WePayConnectionError<wepay.exceptions.WePayConnectionError>`

        """
        headers = {
            'Content-Type': 'application/json', 
            'User-Agent': 'Python WePay SDK (third party)'
        }
        url = self.api_endpoint + uri
        if token is not None:
            warnings.warn("'token' parameter is deprecated and is here only "
                          "for compatibility with official Python WePay SDK. "
                          "Use 'access_token' instead.", DeprecationWarning)
        access_token = access_token or token or self.access_token
        headers['Authorization'] = 'Bearer %s' % access_token

        api_version = api_version or self.api_version
        if not api_version is None:
            headers['Api-Version'] = api_version
        params = params or {}
        return self._post(url, params, headers, timeout or self._timeout)

       
    def get_authorization_url(self, redirect_uri, client_id, options=None,
                              scope=None):
        """Returns a URL to send the user to in order to get authorization.  After
        getting authorization the user will return to redirect_uri.  Optionally,
        scope can be set to limit permissions, and the options dict can be
        loaded with any combination of state, user_name or user_email.

        .. note::

           This function is here for compatibilty with official Python WePay SDK 
           only, use :func:`WePay.oauth2.authorize` instead.           
        
        :param str redirect_uri: The URI to redirect to after a authorization.
        :param str client_id: The client ID issued by WePay to your app.
        :keyword dict options: Allows for passing additional values to the
            authorize call, aside from scope, redirect_uri, and etc.
        :keyword str scope: A comma-separated string of permissions.

        """
        warnings.warn("'get_authorization_url' is deprecated and is here only "
                      "for compatibility with official Python WePay SDK. "
                      "Use 'WePay.oauth2.authorize' instead.", DeprecationWarning)
        if not options:
            options = {}
        if not scope:
            scope = "manage_accounts,collect_payments," \
                    "view_user,preapprove_payments," \
                    "manage_subscriptions,send_money"
        return self.oauth2.authorize(client_id, redirect_uri, scope, **options)

    
    def get_token(self, *args, **kwargs):
        """Calls wepay.com/v2/oauth2/token to get an access token. Sets the
        access_token for the WePay instance and returns the entire response as a
        dict. Should only be called after the user returns from being sent to
        get_authorization_url.

        .. note::

           This function is here for compatibilty with official Python WePay SDK
           only, use :func:`WePay.oauth2.token` instead.

        :param str redirect_uri: The same URI specified in the
            :py:meth:`get_authorization_url` call that preceded this.
        :param str client_id: The client ID issued by WePay to your app.
        :param str client_secret: The client secret issued by WePay
            to your app.
        :param str code: The code returned by :py:meth:`get_authorization_url`.

        """
        warnings.warn("'get_token' is deprecated and is here only "
                      "for compatibility with official Python WePay SDK. "
                      "Use 'WePay.oauth2.token' instead.", DeprecationWarning)
        response = self.oauth2.token(*args, **kwargs)
        self.access_token = response['access_token']
        return response


    def _backwards(self):
        for cls in self.supported_calls:
            inst = getattr(self, cls.call_name)
            for f_name in dir(cls):
                try:
                    if not f_name.startswith('_'):
                        c_name = "%s_%s" % (cls.call_name, f_name)
                        setattr(self, c_name, getattr(inst, f_name))
                except AttributeError: pass


    def _backward_wepay_warning_getter(self):
        from wepay.exceptions import WePayWarning
        warnings.warn(
            "WePayWarning was moved to wepay.exeptions module.", DeprecationWarning)
        return WePayWarning

    WePayWarning = property(_backward_wepay_warning_getter)