from wepay.calls.base import Call

class CreditCard(Call):
    """The /credit_card API calls"""

    call_name = 'credit_card'

    def __call__(self, client_id, client_secret, credit_card_id, **kwargs):
        """Call documentation: `/credit_card
        <https://www.wepay.com/developer/reference/credit_card#lookup>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        return self.make_call(self, params, kwargs)
    allowed_params = ['client_id', 'client_secret', 'credit_card_id']
    control_keywords = ['batch_mode']


    def create(self, client_id, cc_number, cvv, expiration_month,
               expiration_year, user_name, email, address, original_ip,
               original_device, **kwargs):
        """Call documentation: `/credit_card/create
        <https://www.wepay.com/developer/reference/credit_card#create>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'client_id': client_id,
            'cc_number': cc_number, 
            'cvv': cvv,
            'expiration_month': expiration_month,
            'expiration_year': expiration_year,
            'user_name': user_name,
            'email': email,
            'address': address,
            'original_ip': original_ip,
            'original_device': original_device
        }
        return self.make_call(self.create, params, kwargs)
    create.allowed_params = [
        'client_id', 'cc_number', 'cvv', 'expiration_month', 'expiration_year',
        'user_name', 'email', 'address', 'original_ip', 'original_device'
    ]
    create.control_keywords = ['batch_mode']


    def authorize(self, client_id, client_secret, credit_card_id, **kwargs):
        """Call documentation: `/credit_card/authorize
        <https://www.wepay.com/developer/reference/credit_card#authorize>`_,
        plus extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        return self.make_call(self.authorize, params, kwargs)
    authorize.allowed_params = ['client_id', 'client_secret', 'credit_card_id']
    authorize.control_keywords = ['batch_mode']


    def find(self, client_id, client_secret, **kwargs):
        """Call documentation: `/credit_card/find
        <https://www.wepay.com/developer/reference/credit_card#find>`_, plus
        extra keyword parameter:
        
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
        return self.make_call(self.find, params, kwargs)
    find.allowed_params = [
        'client_id', 'client_secret', 'reference_id', 'limit', 'start',
        'sort_order'
    ]
    find.control_keywords = ['batch_mode']


    def delete(self, client_id, client_secret, credit_card_id, **kwargs):
        """Call documentation: `/credit_card/delete
        <https://www.wepay.com/developer/reference/credit_card#delete>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        """
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'credit_card_id': credit_card_id
        }
        return self.make_call(self.delete, params, kwargs)
    delete.allowed_params = ['client_id', 'client_secret', 'credit_card_id']
    delete.control_keywords = ['batch_mode']
