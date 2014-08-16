
Python WePay SDK (third party)
==============================

.. image:: https://travis-ci.org/lehins/python-wepay.svg?branch=master   
   :target: https://travis-ci.org/lehins/python-wepay
   :alt: Travis-CI

.. image:: https://coveralls.io/repos/lehins/python-wepay/badge.png?branch=master 
   :target: https://coveralls.io/r/lehins/python-wepay?branch=master 
   :alt: Tests Coverage

.. image:: https://pypip.in/d/python-wepay/badge.png
    :target: https://crate.io/packages/python-wepay/
    :alt: Number of PyPI downloads


Features
--------

* Make API calls in a very natural pythonic way, ex:

.. code-block:: python

    >>> api = WePay(production=False, access_token='STAGE_243...')
    >>> response = api.credit_card.create(client_id, cc_number, ..., original_ip='127...')
    >>> api.credit_card.authorize(client_id, client_secret, response['credit_card_id'])

* Validation of all required and optional parameters to each one of the calls.
* Very easy construction of batch calls, simply by passing ``batch_mode=True`` to
  a call, ex:

.. code-block:: python

    >>> calls = []
    >>> calls.append(api.credit_card.authorize(
    ...                  client_id, client_secret, response['credit_card_id'],
    ...                  batch_mode=True, batch_reference_id='ref_id_1234'))
    >>> # append more calls ...
    >>> response = api.batch.create(client_id, client_secret, calls)


About
-----

This package started as a part of `Django WePay Application
<https://github.com/lehins/django-wepay>`_, but I soon realized it could be
useful to other developers in Python community that do not use `Django
<https://djangoproject.com>`_. Originally it meant to be an extension of an
official `Python WePay SDK <https://github.com/wepay/Python-SDK>`_, but instead
it became a replacement with full compatibilty with official WePay version.
This package is also listed as a `third party Python SDK on WePay
<https://www.wepay.com/developer/resources/sdks>`_.

Status
------

Production.

Requirements
------------

* Python >= 2.7 or >= 3.2
* Registered Application with WePay `production <https://wepay.com>`_ site or
  it's `development <https://stage.wepay>`_ clone.
* `six <https://pypi.python.org/pypi/six>`_.
* `requests <http://docs.python-requests.org/en/latest/>`_ (optional):
* `mock <https://pypi.python.org/pypi/mock>`_ (optional, for tests only)

Installation
------------
::

    pip install python-wepay


Documentation
-------------

http://python-wepay.readthedocs.org/en/latest/index.html

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/lehins/python-wepay/blob/master/LICENSE>`_ file for more details.
