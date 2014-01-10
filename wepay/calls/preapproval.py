from wepay.calls.base import Call

class Preapproval(Call):
    """ The /preapproval API calls"""

    call_name = 'preapproval'
    
    def __call__(self, preapproval_id, **kwargs):
        """Call documentation: `/preapproval
        <https://www.wepay.com/developer/reference/preapproval#lookup>`_, plus
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
            'preapproval_id': preapproval_id
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['preapproval_id']


    def find(self, **kwargs):
        """Call documentation: `/preapproval/find
        <https://www.wepay.com/developer/reference/preapproval#find>`_, plus
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
        params = {}
        return self.make_call(self.find, params, kwargs)
    find.allowed_params = [
        'account_id', 'state', 'reference_id', 'start', 'limit', 'sort_order', 
        'last_checkout_id', 'shipping_fee',
    ]


    def create(self, short_description, period, **kwargs):
        """Call documentation: `/preapproval/create
        <https://www.wepay.com/developer/reference/preapproval#create>`_, plus
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
            'short_description': short_description,
            'period': period
        }
        return self.make_call(self.create, params, kwargs)
    create.allowed_params = [
        'account_id', 'amount', 'currency', 'short_description', 'period',
        'reference_id', 'app_fee', 'fee_payer', 'redirect_uri', 'callback_uri',
        'fallback_uri', 'require_shipping', 'shipping_fee', 'charge_tax',
        'payer_email_message','long_description', 'frequency',
        'start_time','end_time', 'auto_recur', 'mode', 'prefill_info',
        'funding_sources', 'payment_method_id', 'payment_method_type'
    ]


    def cancel(self, preapproval_id, **kwargs):
        """Call documentation: `/preapproval/cancel
        <https://www.wepay.com/developer/reference/preapproval#cancel>`_, plus
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
            'preapproval_id': preapproval_id
        }
        return self.make_call(self.cancel, params, kwargs)
    cancel.allowed_params = ['preapproval_id']


    def modify(self, preapproval_id, **kwargs):
        """Call documentation: `/preapproval/modify
        <https://www.wepay.com/developer/reference/preapproval#modify>`_, plus
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
            'preapproval_id': preapproval_id
        }
        return self.make_call(self.modify, params, kwargs)
    modify.allowed_params = ['preapproval_id', 'callback_uri']

