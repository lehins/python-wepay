######################################################################
python-wepay
######################################################################

**Third Party Python WePay SDK**

About
-----

This package started as a part of `Django WePay Application
<https://github.com/lehins/django-wepay>`_, but I soon realized it could be
useful to other developers in Python community that do not use `Django
<https://djangoproject.com>`_. Originally it meant to be an extension of an
official `Python WePay SDK <https://github.com/wepay/Python-SDK>`_, but instead
it became a replacement with full compatibilty with official WePay version.

Status
------

Production.

Requirements
------------

* Registered Application with WePay `production <https://wepay.com>`_ site or
  it's `development <https://stage.wepay>`_ clone.
* `six <https://pypi.python.org/pypi/six>`_.
* `requests <http://docs.python-requests.org/en/latest/>`_ (optional):
* `mock <https://pypi.python.org/pypi/mock>`_ (optional, for tests only)

Installation
------------

    pip install python-wepay

Optional:

    pip install requests
    

Documentation
-------------

http://python-wepay.readthedocs.org/en/latest/index.html
