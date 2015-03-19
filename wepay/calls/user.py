import warnings
from wepay.calls.base import Call

class User(Call):
    """ The /user API calls """

    call_name = 'user'

    def __call__(self, **kwargs):
        """Call documentation: `/user
        <https://www.wepay.com/developer/reference/user#lookup>`_, plus extra
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
        return self.make_call(self, {}, kwargs)
    allowed_params = []


    def __modify(self, **kwargs):
        """Call documentation: `/user/modify
        <https://www.wepay.com/developer/reference/user#modify>`_, plus extra
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
        return self.make_call(self.__modify, {}, kwargs)
    __modify.allowed_params = ['callback_uri']
    modify = __modify


    def __register(self, client_id, client_secret, email, scope, first_name,
                   last_name, original_ip, original_device, **kwargs):
        """Call documentation: `/user/register
        <https://www.wepay.com/developer/reference/user#register>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        .. note ::

            This call is NOT supported by API versions older then '2014-01-08'.

        """
        params = {
            'client_id': client_id, 
            'client_secret': client_secret, 
            'email': email, 
            'scope': scope, 
            'first_name': first_name,
            'last_name': last_name, 
            'original_ip': original_ip, 
            'original_device': original_device
        }
        return self.make_call(self.__register, params, kwargs)
    __register.allowed_params = [
        'client_id', 'client_secret', 'email', 'scope', 'first_name', 'last_name', 
        'original_ip', 'original_device', 'redirect_uri', 'callback_uri', 
        'tos_acceptance_time'
    ]
    __register.control_keywords = ['batch_mode']
    register = __register


    def __send_confirmation(self, **kwargs):
        """Call documentation: `/user/resend_confirmation
        <https://www.wepay.com/developer/reference/user#resend_confirmation>`_, plus
        extra keyword parameter:
        
        :keyword bool batch_mode: turn on/off the batch_mode, see 
           :class:`wepay.api.WePay`

        :keyword str batch_reference_id: `reference_id` param for batch call,
           see :class:`wepay.api.WePay`

        :keyword str api_version: WePay API version, see
           :class:`wepay.api.WePay`

        .. note ::

            This call is NOT supported by API versions older then '2014-01-08'.

        """
        return self.make_call(self.__send_confirmation, {}, kwargs)
    __send_confirmation.allowed_params = ['email_message']
    __send_confirmation.control_keywords = ['batch_mode']
    send_confirmation = __send_confirmation

    
    def resend_confirmation(self, *args, **kwargs):
        """:meth:`User.send_confirmation` should be used instead.

        .. warning ::

            As of 2015-02-25 this is a deprecated call and has been renamed.
        """
        warnings.warn(
            "/user/resend_confirmation API call has been renamed to: "
            "/user/send_confirmation on 2015-02-25. Will be removed in 1.5 version.",
            DeprecationWarning
        )
        return self.send_confirmation(*args, **kwargs)
