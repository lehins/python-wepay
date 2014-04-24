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

Methods that can perform calls on behalf of WePay User accept optionall keyword
argument ``access_token``, which will then be used to perform a call instead of
one the :class:`wepay.WePay` class was instantiated with. Methods that can be
used in a '/batch/create' call also accept ``batch_mode`` keyword argument,
which instead of making a call will force it to return a dictionary, which can
be used later on to perform a :func:`wepay.WePay.batch_create` call. An
unrecognized keyword passed to those functions will produce a warning and an
actuall error from WePay, if it is in fact an unrecognized parameter.

Quick Example::
    
    >>> WEPAY_ACCESS_TOKEN = 'STAGE_243b....'
    >>> WEPAY_CLIENT_ID = 123456
    >>> WEPAY_CLIENT_SECRET = '1a2b3c4e5f'
    >>> WEPAY_DEFAULT_SCOPE = "manage_accounts,collect_payments,view_balance,view_user,preapprove_payments,send_money"
    >>> REDIRECT_URI = 'https://example.com/user/wepay/redirect'
    >>> api = WePay(production=False, access_token=WEPAY_ACCESS_TOKEN)
    >>> api.app(WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET)
    {u'status': u'approved', u'theme_object': .....}
    >>> redirect_uri = api.oauth2.authorize(WEPAY_CLIENT_ID, REDIRECT_URI, WEPAY_DEFAULT_SCOPE, user_email='lehins@.....ru')
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

.. include:: ../../CHANGES.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

