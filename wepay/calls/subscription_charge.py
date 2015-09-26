from wepay.calls.base import Call

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
