from wepay.calls.base import Call

class Account(Call):
    """ The /account API calls"""

    call_name = 'account'

    def __call__(self, account_id, **kwargs):
        """Call documentation: `/account
        <https://www.wepay.com/developer/reference/account#lookup>`_, plus extra
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
        return self.make_call(self, params, kwargs)
    allowed_params = ['account_id']


    def find(self, **kwargs):
        """Call documentation: `/account/find
        <https://www.wepay.com/developer/reference/account#find>`_, plus extra
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
        params = {}
        return self.make_call(self.find, params, kwargs)
    find.allowed_params = ['name', 'reference_id', 'sort_order']


    def create(self, name, description, **kwargs):
        """Call documentation: `/account/create
        <https://www.wepay.com/developer/reference/account#create>`_, plus extra
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
            'name': name,
            'description': description
        }
        return self.make_call(self.create, params, kwargs)
    create.allowed_params = [
        'name', 'description', 'reference_id', 'type', 'image_uri', 'gaq_domains', 
        'theme_object', 'mcc', 'callback_uri', 'country', 'currencies'
    ]


    def modify(self, account_id, **kwargs):
        """Call documentation: `/account/modify
        <https://www.wepay.com/developer/reference/account#modify>`_, plus extra
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
        return self.make_call(self.modify, params, kwargs)
    modify.allowed_params = [
        'account_id', 'name', 'description', 'reference_id', 'image_uri', 
        'gaq_domains', 'theme_object', 'callback_uri'
    ]


    def delete(self, account_id, **kwargs):
        """Call documentation: `/account/delete
        <https://www.wepay.com/developer/reference/account#delete>`_, plus extra
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
        return self.make_call(self.delete, params, kwargs)
    delete.allowed_params = ['account_id', 'reason']


    def get_update_uri(self, account_id, **kwargs):
        """Call documentation: `/account/get_update_uri
        <https://www.wepay.com/developer/reference/account#update_uri>`_, plus extra
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
        return self.make_call(self.get_update_uri, params, kwargs)
    get_update_uri.allowed_params = ['account_id', 'mode', 'redirect_uri']
    

    def get_reserve_details(self, account_id, **kwargs):
        """Call documentation: `/account/get_reserve_details
        <https://www.wepay.com/developer/reference/account#reserve>`_, plus extra
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
        return self.make_call(self.get_reserve_details, params, kwargs)
    get_reserve_details.allowed_params = ['account_id', 'currency']


    # deprecated calls

    def balance(self, account_id, **kwargs):
        """Call documentation: `/account/balance
        <https://www.wepay.com/developer/reference/account#balance>`_, plus
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

        .. warning ::

            This call is depricated as of API version '2014-01-08'.

        """
        params = {
            'account_id': account_id
        }
        return self.make_call(self.balance, params, kwargs)
    balance.allowed_params = ['account_id']

        
    def add_bank(self, account_id, **kwargs):
        """Call documentation: `/account/add_bank
        <https://www.wepay.com/developer/reference/account#add_bank>`_, plus
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

        .. warning ::

            This call is depricated as of API version '2014-01-08'.

        """
        params = {
            'account_id': account_id
        }
        return self.make_call(self.add_bank, params, kwargs)
    add_bank.allowed_params = ['account_id', 'mode', 'redirect_uri']

        
    def set_tax(self, account_id, taxes, **kwargs):
        """Call documentation: `/account/set_tax
        <https://www.wepay.com/developer/reference/account#set_tax>`_, plus
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

        .. warning ::

            This call is depricated as of API version '2014-01-08'.

        """
        params = {
            'account_id': account_id,
            'taxes': taxes
        }
        return self.make_call(self.set_tax, params, kwargs)
    set_tax.allowed_params = ['account_id', 'taxes']


    def get_tax(self, account_id, **kwargs):
        """Call documentation: `/account/get_tax
        <https://www.wepay.com/developer/reference/account#get_tax>`_, plus
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

        .. warning ::

            This call is depricated as of API version '2014-01-08'.

        """
        params = {
            'account_id': account_id
        }
        return self.make_call(self.get_tax, params, kwargs)
    get_tax.allowed_params = ['account_id']
