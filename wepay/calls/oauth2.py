import urllib
from wepay.calls.base import Call

class OAuth2(Call):
    """ API OAuth2 Endpoints """

    call_name = 'oauth2'

    def authorize(self, client_id, redirect_uri, scope, 
                  state=None, user_name=None, user_email=None):
        """Documentation: `/oauth2/authorize
        <https://www.wepay.com/developer/reference/oauth2#authorize>`_.

        .. note::
    
           This is not an API call but an actual uri that you send the user to.

        """
        options = {
            'client_id': client_id,
            'redirect_uri': redirect_uri,
            'scope': scope
        }
        if not user_name is None:
            options['user_name'] = user_name
        if not user_email is None:
            options['user_email'] = user_email
        if not state is None:
            options['state'] = state
        return '%s/oauth2/authorize?%s' % (
            self.api.browser_endpoint, urllib.urlencode(options))


    def __token(self, client_id, redirect_uri, client_secret, code, **kwargs):
        """Call documentation: `/oauth2/token
        <https://www.wepay.com/developer/reference/oauth2#token>`_, plus extra
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
            'redirect_uri': redirect_uri,
            'client_secret': client_secret,
            'code': code
        }
        return self.make_call(self.__token, params, kwargs)
    __token.allowed_params = [
        'client_id', 'redirect_uri', 'client_secret', 'code', 'callback_uri',
    ]
    __token.control_keywords = ['batch_mode']
    token = __token