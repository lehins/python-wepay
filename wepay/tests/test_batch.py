from wepay.tests import CallBaseTestCase

class BatchTestCase(CallBaseTestCase):

    def test_batch_find(self):
        args = [
            ('client_id', 67890),
            ('client_secret', 'secret_6789'),
            ('calls', [
                {
                    'call': '/preapproval',
                    'authorization': 'access_token_call_0',
                    'reference_id': 'reference_id_call_0',
                    'parameters': {
                        'preapproval_id': 12345
                    }
                },
                {
                    'call': '/preapproval/find',
                    'authorization': 'access_token_call_1',
                    'reference_id': 'reference_id_call_1',
                    'parameters': {
                        'account_id': 54321,
                        'state': 'expired',
                        'reference_id': 'ref_preapproval_123',
                        'start': 10,
                        'limit': 17,
                        'last_checkout_id': 221651,
                        'sort_order': 'ASC',
                        'shipping_fee': 34.05
                    }
                }
            ])
        ]
        call_0 = args[2][1][0]
        self.api.preapproval(
            call_0['parameters']['preapproval_id'], batch_mode=True, 
            batch_reference_id=call_0['reference_id'], access_token=call_0['authorization'])
        call_1 = args[2][1][1]
        self.api.preapproval.find(
            batch_mode=True, batch_reference_id=call_1['reference_id'], 
            access_token=call_1['authorization'], **call_1['parameters'])
        self._test_call('/batch/create', args, {})
