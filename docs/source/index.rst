.. python-wepay documentation master file, created by
   sphinx-quickstart on Tue Sep 10 20:53:15 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-wepay's documentation!
========================================

**Python WePay SDK (third party)**

Based on official `Python Wepay SDK <https://github.com/wepay/Python-SDK>`_, and designed to be completely compatible with it.

Before using this package get yourself familiar with actual WePay `API Documentation <https://www.wepay.com/developer>`_.

`WePay <https://wepay.com>`_ is a great service, highly recommend it.


.. automodule:: wepay
   :members:

---------
Contents:
---------

.. toctree::
   :glob:

   wepay*

------------
Installation
------------
::

    pip install python-wepay


------------
Latest build
------------

Forkme on Github: `python-wepay <https://github.com/lehins/python-wepay>`_

----------------
Quickstart Guide
----------------

This package suppose to make it easier to construct and send API calls in more
Pythonic way rather than building dictionary with parameters and simply sending
it to WePay servers.

Just like with official SDK the core of this package is :class:`wepay.WePay`
class, which needs to be instantiated with valid ``access_token`` and
``production`` arguments of your WePay Application, after which API calls can be
made. All methods within ``WePay`` object mimic API calls from official
`Documentation <https://www.wepay.com/developer>`_ in the way that normally
would be expected, call names are directly mapped into functions with same names
moreover all required parameters are passed to functions as ``args`` and
optional ones as ``kwargs``.

Methods that can perform calls on behalf of WePay User accept optional keyword
argument ``access_token``, which will then be used to perform a call instead of
one the :class:`wepay.WePay` class was instantiated with. Methods that can be
used in a '/batch/create' call also accept ``batch_mode`` keyword argument,
which instead of making a call will force it to return a dictionary, that can be
used later on to perform a :func:`wepay.WePay.batch_create` call. Additionally
each call accepts ``api_version`` and ``timeout`` keyword arguments, which
specify a WePay API version and connection timeout respectively. An unrecognized
keyword passed to those functions will produce a warning and an actuall error
from WePay, if it is in fact an unrecognized parameter.

Quick Example

.. code-block:: python
    
    >>> WEPAY_ACCESS_TOKEN = 'STAGE_243b....'
    >>> WEPAY_CLIENT_ID = 123456
    >>> WEPAY_CLIENT_SECRET = '1a2b3c4e5f'
    >>> WEPAY_DEFAULT_SCOPE = "manage_accounts,collect_payments,view_balance,view_user,preapprove_payments,send_money"
    >>> REDIRECT_URI = 'https://example.com/user/wepay/redirect'
    >>> api = WePay(production=False, access_token=WEPAY_ACCESS_TOKEN)
    >>> api.app(WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET)
    {u'status': u'approved', u'theme_object': .....}
    >>> redirect_uri = api.oauth2.authorize(WEPAY_CLIENT_ID, REDIRECT_URI, WEPAY_DEFAULT_SCOPE, user_email="user@example.com")
    >>> redirect_uri
    'https://stage.wepay.com/v2/oauth2/authorize?scope=manage_accounts%2C........'
    >>> # Get the 'code' from url... (for detailed instructions on how to do it follow WePay documentation)
    >>> response = api.oauth2.token(WEPAY_CLIENT_ID, redirect_uri, WEPAY_CLIENT_SECRET, '8c3e4aca23e1ed7.....', callback_uri='https://example.com/wepay/ipn/user')
    >>> response
    {u'access_token': u'STAGE_f87....', u'token_type': u'BEARER', u'user_id': 87654321}
    >>> access_token = response['access_token']
    >>> api.account.create("Test Account", "Account will be used to make a lot of money", access_token=access_token)
    {u'account_id': 1371765417, u'account_uri': u'https://stage.wepay.com/account/1371765417'}
    >>> api.checkout.create(1371765417, "Short description.....


--------------
Error Handling
--------------

Whenever you perform an API call and it results in an error, the are two possible
causes:

* either there is a problem connecting to a WePay server (internet connection is
  down, WePay server is down, request times out, ssl validation failed, etc) in
  which case a call will raise
  :exc:`~wepay.exceptions.WePayConnectionError`. If the cause is
  timeout, consider increasing ``timeout`` value during :class:`~wepay.api.WePay`
  initialization or on per call basis, in particular for
  :meth:`batch.create()<wepay.calls.batch.Batch.create>` call, since it can take a while for
  WePay to process up to 50 batched calls in one request.
* or there is a problem processing the actual call due to a `WePay documented
  <https://www.wepay.com/developer/reference/errors>`_ reason or for some other
  unknown reason, like an implemetation error on WePay side or a malformed
  response for instance. In this case either
  :exc:`~wepay.exceptions.WePayServerError` or
  :exc:`~wepay.exceptions.WePayClientError` will be raised.

So far, I've noticed that
:exc:`WePayServerError's<wepay.exceptions.WePayServerError>` happen due to
incorect usage of API (ex. unrecognized api call) or a problem with WePay, while
:exc:`WePayClientError's<wepay.exceptions.WePayClientError>` can happen anytime,
for instance in case of a credit card decline. I would recommend handling them
in a separate way, but you can also simply catch
:exc:`~wepay.exceptions.WePayHTTPError` and handle it depending on
:attr:`~wepay.exceptions.WePayHTTPError.error_code` and
:attr:`~wepay.exceptions.WePayHTTPError.status_code`. Above mentioned exceptions
also give you access to the actual HTTP Error:
:attr:`~wepay.exceptions.WePayHTTPError.http_error` which will carry a response
body inside, hence can give some more information on the nature of the error. If
you really don't care about response body or HTTP status code, it is possible to
just always catch :exc:`~wepay.exceptions.WePayError`, which carries only
information documented by WePay.

Also note, that depending on the library used for making calls, different types
of errors will be contained in
:attr:`~wepay.exceptions.WePayHTTPError.http_error` and
:attr:`~wepay.exceptions.WePayConnectionError.error`. Refer to their
documentation to find detailed information: `requests
<http://docs.python-requests.org/en/latest/>`_ or `urllib
<https://docs.python.org/3/library/urllib.html#module-urllib>`_

So here is an example:

.. code-block:: python

   from wepay import WePay
   from wepay.exceptions import WePayClientError, WePayServerError, WePayConnectionError

   def get_withdrawal_uri(account_id, access_token):
       api = WePay(production=True, access_token=access_token, silent=True)
       try:
           response = api.account(account_id)
           for balance in response['balances']:
               if balance['currency'] == "USD":
                   usd_balance = balance['balance']
                   break
           if usd_balance > 0:
               response = api.withdrawal.create(account_id, currency="USD", note="Need Money!")
               return response['withdrawal_uri']
       except WePayClientError as exc:
           if exc.error_code == 3003:
               print "Sorry, this account was deleted"
           elif exc.error_code == 3002:
               print "Dummy, you used a wrong access_token"
           elif exc.error_code == 6002:
               print "What are you doing? You are not allowed to get money"
           else:
               print exc
       except WePayServerError as exc:
           print "Oh oh, something went wrong, please contact api@wepay.com"
           print exc
       except WePayConnectionError as exc:
           print "there was a problem connecting to WePay, please try again later"
           print exc

So now you could use this function to get a url where to send a user in case
there is a positive balance. It's kind of useless, since WePay schedules
Withdrawals automatically and it only supports "USD" currency at the moment,
moreover it's easier to handle a 3005 ``error_code``, instead of checking a
balance first, but I hope it's good enough for demonstrating error handling.

.. code-block:: python

    >>> from myapp.settings import WEPAY_ACCOUNT_ID, WEPAY_ACCESS_TOKEN
    >>> withdrawal_uri = get_withdrawal_uri(WEPAY_ACCOUNT_ID, WEPAY_ACCESS_TOKEN)
    >>> if withdrawal_uri:
    >>>     # send user to this uri to finish withdrawal creation process.


---------------
Customizing SDK
---------------

Let's say you would like default values provided right away, or customize calls
in some other handy way. For example you would like to supply some default
values related specifically to your application and turn off objects you will
never use:

.. code-block:: python

    from wepay import WePay, calls
    from wepay.utils import cached_property

    from myapp.settings import WEPAY_PRODUCTION, WEPAY_ACCESS_TOKEN, WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET


    class App(calls.App):

        def __call__(self, **kwargs):
            return super(App, self).__call__(WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET, **kwargs)

        def modify(self, **kwargs):
            return super(App, self).modify(WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET, **kwargs)


    class User(calls.User):

        def register(self, *args, **kwargs):
            return super(User, self).register(
                WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET, *args, **kwargs)


    class Batch(calls.Batch):

        def create(self, calls, **kwargs):
            return super(Batch, self).create(
                WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET, calls, **kwargs)


    class MyWePay(WePay):
        credit_card = None
        subscription_plan = None
        subscription = None
        subscription_charge = None

        def __init__(self, **kwargs):
             kwargs.setdefault('production', WEPAY_PRODUCTION)
             kwargs.setdefault('timeout', 45)
             kwargs.setdefault('access_token', WEPAY_ACCESS_TOKEN)
             kwargs['silent'] = True
             super(MyWePay, self).__init__(**kwargs)

        @cached_property
        def app(self):
            return App(self)
    
        @cached_property
        def user(self):
            return User(self)

        @cached_property
        def batch(self):
            return Batch(self)


This will effectively supply all of your WePay Application related info, for all
of the calls you are planning on using, since other objects don't rely on
``client_id`` or ``client_secret``, with an exception of App level Preapprovals,
of course. ``cached_property`` decorator alows lazy call initialization and,
although you could use a regular ``property`` decorator, ``cached_property`` is
more efficient, since it initializes a call object only once per `~wepay.api.WePay` instance,
instead of every time a call is performed.

------------
Project Info
------------

.. toctree::
   :maxdepth: 1

   changelog
   authors
   license

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

