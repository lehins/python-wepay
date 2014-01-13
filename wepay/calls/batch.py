from wepay.calls.base import Call

class Batch(Call):
    """ The /batch API calls """

    call_name = 'batch'

    def __create(self, client_id, client_secret, calls, **kwargs):
        """Call documentation: `/batch/create
        <https://www.wepay.com/developer/reference/batch#create>`_, plus extra
        keyword parameter:
        
        :keyword str access_token: will be used instead of instance's
            ``access_token``

        """
        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'calls': calls
        }
        return self.make_call(self.__create, params, kwargs)
    __create.allowed_params = ['client_id', 'client_secret', 'calls']
    __create.control_kwargs = ['access_token']
    create = __create