from wepay.calls.base import Call

class Checkout(Call):
    """ The /checkout API calls """

    call_name = 'checkout'

    def __call__(self, checkout_id, **kwargs):
        """Call documentation: `/checkout
        <https://www.wepay.com/developer/reference/checkout#lookup>`_, plus
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
            'checkout_id': checkout_id
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['checkout_id']


    def __find(self, account_id, **kwargs):
        """Call documentation: `/checkout/find
        <https://www.wepay.com/developer/reference/checkout#find>`_, plus extra
        keyword parameters:
        
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
            'account_id': account_id
        }
        return self.make_call(self.__find, params, kwargs)
    __find.allowed_params = [
        'account_id', 'start', 'limit', 'reference_id', 'state', 
        'preapproval_id', 'start_time', 'end_time', 'sort_order', 'shipping_fee'
    ]
    find = __find

    def __create(self, account_id, short_description, type, amount, **kwargs):
        """Call documentation: `/checkout/create
        <https://www.wepay.com/developer/reference/checkout#create>`_, plus
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
            'account_id': account_id,
            'short_description': short_description,
            'type': type,
            'amount': amount
        }
        return self.make_call(self.__create, params, kwargs)
    __create.allowed_params = [
        'account_id', 'short_description', 'type', 'currency', 'amount', 
        'long_description', 'payer_email_message', 'payee_email_message', 'reference_id', 
        'app_fee', 'fee_payer', 'redirect_uri', 'callback_uri', 'fallback_uri', 
        'auto_capture', 'require_shipping', 'shipping_fee', 'charge_tax', 'mode', 
        'preapproval_id', 'prefill_info', 'funding_sources', 'payment_method_id', 
        'payment_method_type'
    ]
    create = __create


    def __cancel(self, checkout_id, cancel_reason, **kwargs):
        """Call documentation: `/checkout/cancel
        <https://www.wepay.com/developer/reference/checkout#cancel>`_, plus
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
            'checkout_id': checkout_id,
            'cancel_reason': cancel_reason
        }
        return self.make_call(self.__cancel, params, kwargs)
    __cancel.allowed_params = ['checkout_id', 'cancel_reason']
    cancel = __cancel

    def __refund(self, checkout_id, refund_reason, **kwargs):
        """Call documentation: `/checkout/refund
        <https://www.wepay.com/developer/reference/checkout#refund>`_, plus
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
            'checkout_id': checkout_id,
            'refund_reason': refund_reason
        }
        return self.make_call(self.__refund, params, kwargs)
    __refund.allowed_params = [
        'checkout_id', 'refund_reason', 'amount', 'app_fee', 'payer_email_message', 
        'payee_email_message'
    ]
    refund = __refund

    def __capture(self, checkout_id, **kwargs):
        """Call documentation: `/checkout/capture
        <https://www.wepay.com/developer/reference/checkout#capture>`_, plus
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
            'checkout_id': checkout_id
        }
        return self.make_call(self.__capture, params, kwargs)
    __capture.allowed_params = ['checkout_id']
    capture = __capture

    def __modify(self, checkout_id, **kwargs):
        """Call documentation: `/checkout/modify
        <https://www.wepay.com/developer/reference/checkout#modify>`_, plus
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
            'checkout_id': checkout_id
        }
        return self.make_call(self.__modify, params, kwargs)
    __modify.allowed_params = ['checkout_id', 'callback_uri']
    modify = __modify
