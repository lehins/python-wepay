"""This module was designed to help making `WePay <https://wepay.com>`_ API calls. 

.. moduleauthor:: lehins <lehins@yandex.ru>
   :platform: independent
"""
from wepay.calls import *
from wepay.utils import Post, cached_property

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
    
    @cached_property
    def oauth2(self):
        """:class:`OAuth2<wepay.calls.oauth2.OAuth2>` call instance."""
        return OAuth2(self)
 
    @cached_property
    def app(self):
        """:class:`App<wepay.calls.app.App>` call instance"""
        return App(self)

    @cached_property
    def user(self):
        """:class:`User<wepay.calls.user.User>` call instance"""
        return User(self)

    @cached_property
    def account(self):
        """:class:`Account<wepay.calls.account.Account>` call instance"""
        return Account(self)

    @cached_property
    def checkout(self):
        """:class:`Checkout<wepay.calls.checkout.Checkout>` call instance"""
        return Checkout(self)

    @cached_property
    def preapproval(self):
        """:class:`Preapproval<wepay.calls.preapproval.Preapproval>` call instance"""
        return Preapproval(self)

    @cached_property
    def withdrawal(self):
        """:class:`Withdrawal<wepay.calls.withdrawal.Withdrawal>` call instance"""
        return Withdrawal(self)

    @cached_property
    def credit_card(self):
        """:class:`CreditCard<wepay.calls.credit_card.CreditCard>` call instance"""
        return CreditCard(self)

    @cached_property
    def subscription_plan(self):
        """:class:`SubscriptionPlan<wepay.calls.subscription_plan.SubscriptionPlan>`
        call instance

        """
        return SubscriptionPlan(self)

    @cached_property
    def subscription(self):
        """:class:`Subscription<wepay.calls.subscription.Subscription>` call instance"""
        return Subscription(self)

    @cached_property
    def subscription_charge(self):
        """:class:`SubscriptionCharge<wepay.calls.subscription_charge.SubscriptionCharge>`
        call instance

        """
        return SubscriptionCharge(self)

    @cached_property
    def batch(self):
        """:class:`Batch<wepay.calls.batch.Batch>` call instance """
        return Batch(self)

    def call(self, uri, params=None, access_token=None, api_version=None, timeout=None):
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
        :return: WePay response as documented per call
        :rtype: dict
        :raises: :exc:`WePayClientError<wepay.exceptions.WePayClientError>`
        :raises: :exc:`WePayServerError<wepay.exceptions.WePayServerError>`
        :raises: :exc:`WePayConnectionError<wepay.exceptions.WePayConnectionError>`

        """
        url = self.api_endpoint + uri
        params = params or {}

        headers = {
            'Content-Type': 'application/json', 
            'User-Agent': 'Python WePay SDK (third party)'
        }
        access_token = access_token or self.access_token
        headers['Authorization'] = 'Bearer %s' % access_token
        api_version = api_version or self.api_version
        if not api_version is None:
            headers['Api-Version'] = api_version

        timeout = timeout or self._timeout
        return self._post(url, params, headers, timeout)
