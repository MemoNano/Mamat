payment_types = [{'payment_id': '24', 'name': 'Tokenized Pay', 'type': 'creditcard', 'is_default': False,
                  'metadata': {'last_four': '0035', 'type': 'DI', 'expiration': '12/21', 'is_expired': False,
                               'postal_code': '60654', 'gateway': None}}]

a = payment_types[-1]["payment_id"]
b = payment_types[0]["payment_id"]

print(a + " \b " + b)
