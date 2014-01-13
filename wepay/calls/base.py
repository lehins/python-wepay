import warnings

class Call(object):
    """ Base class for all API calls """

    _api = None
    floating = ['amount', 'app_fee', 'shipping_fee', 'setup_fee']

    def __init__(self, api):
        self.api = api

    def _update_params(self, params, extra_kwargs, control_keywords):
        if control_keywords is None:
            control_keywords = ['access_token', 'batch_mode']
        control_kwargs = {}
        for key in control_keywords:
            if key in extra_kwargs:
                control_kwargs[key] = extra_kwargs.pop(key)
        if control_kwargs.get('batch_mode', False):
            control_kwargs['reference_id'] = extra_kwargs.pop(
                'batch_reference_id', None)
        control_kwargs['api_version'] = extra_kwargs.pop('api_version', None)
        assert not (
            control_kwargs.get('api_version', None) and 
            control_kwargs.get('batch_mode', False)), \
            "Cannot use 'api_version' and 'batch_mode' in the same call."
        params.update(extra_kwargs)
        return control_kwargs


    def make_call(self, func, params, extra_kwargs):
        """This is a helper function that checks the validity of ``params``
        dictionary by matching it with ``allowed_params`` of a ``func``
        attribute, and then performs a call.  Will issue a `WePayWarning` in
        case of unrecognized parameter, and raise a `WePayError` after making a
        call, in case if it is in fact unrecognized.  If ``batch_mode`` is set
        to ``True`` instead of making a call it will construct a dictionary that
        is ready to be used in :func:`WePay.batch.create` later on, while
        ``refernce_id`` can also be added to it later, as specified by WePay
        Documentation, see :meth:`batch.create<wepay.calls.batch.Batch.create>`

        :param func callable: function making the call
        :param dict params: parameters to include in the call
        :param dict extra_kwargs: extra kwargs passed to a call
        :returns: dict -- depending on ``batch_mode`` flag, either WePay response 
            through calling :func:`call` or a dictionary that is ready 
            to be appended to ``calls`` list that is passed to 
            :meth:`batch.create<wepay.calls.batch.Batch.create`>
        :raises: :mod:`wepay.exceptions.WePayError`

        """
        if hasattr(func, '__name__'):
            uri = '/%s/%s' % (self.call_name, func.__name__[2:])
        else:
            uri = '/%s' % self.call_name
        control_kwargs = self._update_params(
            params, extra_kwargs, getattr(func, 'control_keywords', None))
        access_token = control_kwargs.get('access_token', None)
        api_version = control_kwargs.get('api_version', None)
        if not self.api.silent:
            unrecognized_params = set(params) - set(func.allowed_params)
            if unrecognized_params:
                err_msg = (
                    "At least one of the parameters to the api call: '%s' is "
                    "unrecognized. Allowed parameters are: '%s'. Unrecognized "
                    "parameters are: '%s'." % (uri, ', '.join(func.allowed_params), 
                                               ', '.join(unrecognized_params)))
                if self.api.production:
                    warnings.warn(err_msg, self.api.WePayWarning)
                else:
                    raise self.api.WePayWarning(err_msg)
        
        # in case if param is Decimal
        for name in self.floating:
            if name in params:
                params[name] = float(params[name])
        if control_kwargs.get('batch_mode', False):
            call = {
                'call': uri
            }
            if not access_token is None:
                call['authorization'] = access_token
            if params:
                call['parameters'] = params
            if not control_kwargs['reference_id'] is None:
                call['reference_id'] = control_kwargs['reference_id']
            return call
        return self.api.call(
            uri, params=params, access_token=access_token, api_version=api_version)
