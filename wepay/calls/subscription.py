from wepay.calls.base import Call

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
