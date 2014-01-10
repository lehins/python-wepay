from wepay.calls.base import Call

class App(Call):
    """ The /app API calls """

    call_name = 'app'

    def __call__(self, client_id, client_secret, **kwargs):
        """Call documentation: `/app
        <https://www.wepay.com/developer/reference/app#lookup>`_, plus extra
        keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['client_id', 'client_secret']
    control_keywords = ['batch_mode']


    def modify(self, client_id, client_secret, **kwargs):
        """Call documentation: `/app/modify
        <https://www.wepay.com/developer/reference/app#modify>`_, plus extra
        keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'client_id': client_id,
            'client_secret': client_secret
        }
        return self.make_call(self.modify, params, kwargs)
    modify.allowed_params = [
        'client_id', 'client_secret', 'theme_object', 'gaq_domains'
    ]
    modify.control_keywords = ['batch_mode']