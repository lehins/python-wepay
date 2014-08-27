Changelog
=========

1.4.3
-----

* improved documentation.

1.4.0
-----

* Removed backward compatibility with official `Python WePay SDK <https://github.com/wepay/Python-SDK>`_.
* introduced ``WePayHTTPError``, which is a base exception for both ``WePayClientError`` and ``WePayServerError``
* added ``cached_property`` decorator.
* changed they way calls are initialized. This change doesn't affect the way calls are made.

1.3.5
-----

* Fixed and improved error handling, new exceptions: ``WePayClientError`` and ``WePayServerError``.

1.3.4
-----

* Connection ``timeout`` can be specified on per call basis.

1.3.0
-----

* Python 3 compatible
* Calls are made using `requests <http://docs.python-requests.org/en/latest/>`_
  library by default (if installed), falls back to `urllib
  <https://docs.python.org/3/library/urllib.html#module-urllib>`_ if `requests`
  are not installed or if ``WePay`` is initialized with
  ``use_requests=False``.
* ``WePayConnectionError`` is raised
  in case there is a problem connecting to WePay server, ex. timeout.
* Addition of a full test suit.
* Minor:

  * 'original_ip' and 'original_device' params are now optional in
    `/credit_card/create`.
  * ``silent`` mode is more flexible.
  * Moved ``SubscriptionPlan`` and ``SubscriptionCharge`` to their own modules.
  * Moved ``WePayWarning`` over to ``wepay.exceptions`` module.

1.2.0
-----

* New API version 2014-01-08 changes are reflected in this SDK version:

  * implemented `/user/register` and `user/resend_confirmation` calls.
  * added `/account/get_update_uri` and `/account/get_reserve_details`
  * depricated `/account/add_bank`, `/account/balance`, `/account/get_tax`
    and `/account/set_tax` calls.

* restructured SDK in such a way that all API objects are separate classes, so
  as an example, if we have a WePay instance ``api = WePay()`` and we want to
  make a `/account/find` call, it will look like this ``api.account.find()``
  instead of ``api.account_find()`` (notice **.** instead of **_**), although in
  this version both are equivalent, latter one is depricated and will be removed
  in version 1.3. Despite these changes lookup calls will be the same, ex.
  ``api.account(12345)``.

* Added flexibility to use different API version per call basis. So it is now
  possible to make a depricated call like this: ``api.account.balance(1234,
  api_version='2011-01-15')``

* added ``batch_reference_id`` keyword argument to each call that accepts
  ``batch_mode``


1.1.2
-----

* Added required arguments to `/credit_card/create` call:

  * original_ip
  * original_device

1.1.0
-----

* Added subscription calls:

  * `/subscription_plan`
  * `/subscription`
  * `/subscription_charge`

* Few bug and spelling fixes.

1.0.0
-----

* Initial release
