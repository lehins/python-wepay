"""
.. note:: 

   This module contains API calls that are in Beta mode at WePay. Moreover they
   are also in Beta mode in this SDK and they have not been tested. In case if
   you spot any bugs or have suggestions, please, open an issue on `github
   <https://github.com/lehins/python-wepay>`_ or send me an email to
   lehins@yandex.ru

"""
from wepay.calls.base import Call

class SubscriptionPlan(Call):
    """The /subscription_plan API calls"""

    call_name = 'subscription_plan'

    def __call__(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription_plan
        <https://www.wepay.com/developer/reference/subscription_plan#lookup>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['subscription_plan_id']


    def __find(self, **kwargs):
        """Call documentation: `/subscription_plan/find
        <https://www.wepay.com/developer/reference/subscription_plan#find>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        return self.make_call(self.__find, {}, kwargs)
    __find.allowed_params = ['account_id', 'start', 'limit', 'state', 'reference_id']
    find = __find


    def __create(self, account_id, name, short_description, amount, period,
                 **kwargs):
        """Call documentation: `/subscription_plan/create
        <https://www.wepay.com/developer/reference/subscription_plan#create>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'account_id': account_id,
            'name': name,
            'short_description': short_description,
            'amount': amount,
            'period': period
        }
        return self.make_call(self.__create, params, kwargs)
    __create.allowed_params = [
        'account_id', 'name', 'short_description', 'amount', 'currency',
        'period', 'app_fee', 'callback_uri', 'trial_length', 'setup_fee',
        'reference_id'
    ]
    create = __create


    def __delete(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription_plan/delete
        <https://www.wepay.com/developer/reference/subscription_plan#delete>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(self.__delete, params, kwargs)
    __delete.allowed_params = ['subscription_plan_id', 'reason']
    delete = __delete


    def __get_button(self, account_id, button_type, **kwargs):
        """Call documentation: `/subscription_plan/get_button
        <https://www.wepay.com/developer/reference/subscription_plan#get_button>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'account_id': account_id,
            'button_type': button_type
        }
        return self.make_call(self.__get_button, params, kwargs)
    __get_button.allowed_params = [
        'account_id', 'button_type', 'subscription_plan_id', 'button_text',
        'button_options'
    ]
    get_button = __get_button


    def __modify(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription_plan/modify
        <https://www.wepay.com/developer/reference/subscription_plan#modify>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(self.__modify, params, kwargs)
    __modify.allowed_params = [
        'subscription_plan_id', 'name', 'short_description', 'amount',
        'app_fee', 'callback_uri', 'trial_length', 'setup_fee',
        'update_subscriptions', 'transition_expire_days', 'reference_id'
    ]
    modify = __modify


class Subscription(Call):
    """The /subscription API calls"""

    call_name = 'subscription'

    def __call__(self, subscription_id, **kwargs):
        """Call documentation: `/subscription
        <https://www.wepay.com/developer/reference/subscription#lookup>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['subscription_id']


    def __find(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription/find
        <https://www.wepay.com/developer/reference/subscription#find>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(self.__find, params, kwargs)
    __find.allowed_params = [
        'subscription_plan_id', 'start', 'limit', 'start_time', 'end_time',
        'state', 'reference_id'
    ]
    find = __find
        
        
    def __create(self, subscription_plan_id, **kwargs):
        """Call documentation: `/subscription/create
        <https://www.wepay.com/developer/reference/subscription#create>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_plan_id': subscription_plan_id
        }
        return self.make_call(self.__create, params, kwargs)
    __create.allowed_params = [
        'subscription_plan_id', 'redirect_uri', 'callback_uri',
        'payment_method_id', 'payment_method_type', 'mode', 'quantity',
        'reference_id', 'prefill_info'
    ]
    create = __create


    def __cancel(self, subscription_id, **kwargs):
        """Call documentation: `/subscription/cancel
        <https://www.wepay.com/developer/reference/subscription#cancel>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(self.__cancel, params, kwargs)
    __cancel.allowed_params = ['subscription_id', 'reason']
    cancel = __cancel


    def __modify(self, subscription_id, **kwargs):
        """Call documentation: `/subscription/modify
        <https://www.wepay.com/developer/reference/subscription#modify>`_, plus
        extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(self.__modify, params, kwargs)
    __modify.allowed_params = [
        'subscription_id', 'subscription_plan_id', 'quantity', 'prorate',
        'transition_expire_days', 'redirect_uri', 'callback_uri',
        'payment_method_id', 'payment_method_type', 'reference_id',
        'extend_trial_days',
    ]
    modify = __modify


class SubscriptionCharge(Call):
    """The /subscription_charge API calls"""

    call_name = 'subscription_charge'

    def __call__(self, subscription_charge_id, **kwargs):
        """Call documentation: `/subscription_charge
        <https://www.wepay.com/developer/reference/subscription_charge#lookup>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_charge_id': subscription_charge_id
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['subscription_charge_id']
    

    def __find(self, subscription_id, **kwargs):
        """Call documentation: `/subscription_charge/find
        <https://www.wepay.com/developer/reference/subscription_charge#find>`_,
        plus extra keyword parameters:
        
        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_id': subscription_id
        }
        return self.make_call(self.__find, params, kwargs)
    __find.allowed_params = [
        'subscription_id', 'start', 'limit', 'start_time', 'end_time', 'type',
        'amount', 'state'
    ]
    find = __find
    

    def __refund(self, subscription_charge_id, **kwargs):
        """Call documentation: `/subscription_charge/refund
        <https://www.wepay.com/developer/reference/subscription_charge#refund>`_,
        plus extra keyword parameters:

        :keyword str access_token: will be used instead of instance's
           ``access_token``, with ``batch_mode=True`` will set `authorization`
           param to it's value.

        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'subscription_charge_id': subscription_charge_id
        }
        return self.make_call(self.__refund, params, kwargs)
    __refund.allowed_params = ['subscription_charge_id', 'refund_reason']
    refund = __refund