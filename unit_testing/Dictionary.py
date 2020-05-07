from phc.services.pizzahut.models.service import Service

error_responses2 = {
    'first'  = Service.ERROR_CODE_KEY}
# Service.ERROR_MESSAGE_KEY: 'The email/password you entered is incorrect.'}],


# "second": [{Service.ERROR_CODE_KEY: '0339',
#             Service.ERROR_MESSAGE_KEY: 'The email/password you entered is incorrect.'}],
# "third": [{Service.ERROR_CODE_KEY: '0339',
#            Service.ERROR_MESSAGE_KEY: 'The email / password you entered is incorrect.You have 2 more attempts until your account is locked.'}],


for error_code in error_responses2:
    print(error_code[''])
