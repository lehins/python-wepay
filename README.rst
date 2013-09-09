######################################################################
python-wepay
######################################################################

**Unofficial Python WePay SDK**

About
-----

This package started as a part of `Django WePay Application <https://github.com/lehins/django-wepay>`_, but I soon realized it could be useful to other developers in Python community that do not use `Django <https://djangoproject.com>`_. Originally it meant to be an extension of an official `Python WePay SDK <https://github.com/wepay/Python-SDK>`_, but instead it became a replacement with full compatibilty with official WePay version.

Status
------

Development version. Currently undergoing extensive testing as a part of other application. (there is no reason for me to write separate tests for this package, since all of it's functionality will be tested anyways)

Requirements
------------

* Registered application with WePay `production <https://wepay.com>`_ site or it's `development <https://stage.wepay>`_ clone.

Installation
------------
Can be install from pypi::

    pip install python-wepay
    

Quickstart Guide
----------------

This package suppose to make it easier to construct and send API calls in more Pythonic way rather than building dictionary with parameters and simply sending it to WePay servers.

Just like with official SDK the core of this package is ``WePay`` class, which needs to be instantiated with valid ``access_token`` and ``production`` arguments, after which API calls can be made. All methods within ``WePay`` object mimic API calls from official `Documentation <https://www.wepay.com/developer>`_ in the way that normally would be expected, call names are directly mapped into functions with same names, ex: '/account/create' is ``WePay.account_create``, moreover all required parameters are passed to functions as ``args`` and optional ones as ``kwargs``. There are two helper functions ``WePay.call`` and ``WePay.make_call``, where first one performs a call and latter builds, checks the parameters dictionary and then performs a call. There are also two functions ``get_authorization_url`` and ``get_token``, which are there purely for compatibility with official SDK.

**Important**:
All methods accept optionall keyword argument ``access_token``, which will then be used to perform a call instead of one the ``WePay`` class was created with, and a ``batch_mode`` which instead of making a call will force it to return a dictionary, which can be used later on to perform a ``batch_create`` call. An unrecognized keyword passed to those functions will produce a warning and an actuall error from WePay, if it is in fact an unrecognized parameter.

Quick Example::
    
    >>> WEPAY_ACCESS_TOKEN = 'STAGE_243b....'
    >>> WEPAY_CLIENT_ID = 123456
    >>> WEPAY_CLIENT_SECRET = '1a2b3c4e5f'
    >>> WEPAY_DEFAULT_SCOPE = "manage_accounts,collect_payments,view_balance,view_user,preapprove_payments,send_money"
    >>> REDIRECT_URI = 'https://example.com/user/wepay/redirect'
    >>> api = WePay(production=False, access_token=WEPAY_ACCESS_TOKEN)
    >>> api.app(WEPAY_CLIENT_ID, WEPAY_CLIENT_SECRET)
    {u'status': u'approved', u'theme_object': .....}
    >>> api.oauth2_authorize(WEPAY_CLIENT_ID, REDIRECT_URI, WEPAY_DEFAULT_SCOPE, user_email='lehins@.....ru')
    'https://stage.wepay.com/v2/oauth2/authorize?scope=manage_accounts%2C........'
    >>> # Get the 'code' from url... (for detailed instructions on how to do it follow WePay documentation)
    >>> response = api.oauth2_token(WEPAY_CLIENT_ID, REDIRECT_URI, WEPAY_CLIENT_SECRET, '8c3e4aca23e1ed7.....', callback_uri='https://example.com/wepay/ipn/user')
    >>> response
    {u'access_token': u'STAGE_f87....', u'token_type': u'BEARER', u'user_id': 87654321}
    >>> access_token = response['access_token']
    >>> api.account_create("Test Account", "Account will be used to make a lot of money", access_token=access_token)
    {u'account_id': 1371765417, u'account_uri': u'https://stage.wepay.com/account/1371765417'}
    >>> api.checkout_create(1371765417, "Short description.....


Anyways, you get the idea, just look through the ``api.py`` file for full list of calls. Unfortunately documentation is not written yet, so that will have to suffice for now.

Documentation
-------------

Soon to come. 