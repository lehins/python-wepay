from wepay.calls.base import Call

class Withdrawal(Call):
    """The /withdrawal API calls"""

    call_name = 'withdrawal'

    def __call__(self, withdrawal_id, **kwargs):
        """Call documentation: `/withdrawal
        <https://www.wepay.com/developer/reference/withdrawal#lookup>`_, plus
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
            'withdrawal_id': withdrawal_id
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['withdrawal_id']


    def __find(self, account_id, **kwargs):
        """Call documentation: `/withdrawal/find
        <https://www.wepay.com/developer/reference/withdrawal#find>`_, plus
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
            'account_id': account_id
        }
        return self.make_call(self.__find, params, kwargs)
    __find.allowed_params = ['account_id', 'limit', 'start', 'sort_order']
    find = __find


    def __create(self, account_id, **kwargs):
        """Call documentation: `/withdrawal/create
        <https://www.wepay.com/developer/reference/withdrawal#create>`_, plus
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
            'account_id': account_id
        }
        return self.make_call(self.__create, params, kwargs)
    __create.allowed_params = [
        'account_id', 'currency', 'redirect_uri', 'callback_uri',
        'fallback_uri', 'note', 'mode'
    ]
    create = __create


    def __modify(self, withdrawal_id, **kwargs):
        """Call documentation: `/withdrawal/modify
        <https://www.wepay.com/developer/reference/withdrawal#modify>`_, plus
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
            'withdrawal_id': withdrawal_id
        }
        return self.make_call(self.__modify, params, kwargs)
    __modify.allowed_params = ['withdrawal_id', 'callback_uri']
    modify = __modify

