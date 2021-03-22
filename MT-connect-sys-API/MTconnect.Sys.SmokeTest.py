import json
import requests
# import sys

# sys.stdout = open('D:\Project\kote.txt', 'w')

from Generic import *

# Populate Access Token
data = {'grant_type': grant_type, 'username': Username, 'password': Password, 'scope': Scope}

# Get access token
access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=True,
                                      auth=(client_id, client_secret))

# Print access token
print(access_token_response.text)
tokens = json.loads(access_token_response.text)

headers = {'Authorization': 'Bearer ' + tokens['access_token'], 'Content-Type': 'application/json',
           'DataEncoding': 'UTF-8', 'Accept': 'application/json'}



# Get Entities for Applications
print("Get Entities for Applications")
response = requests.get(url + entities, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result18 = 'PASS'
else:
    result18 = 'FAIL'


# Get All entity setups
print("Get All entity setups")
response = requests.get(url + entity_setups, headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
entity_ID = data['result'][2]['tenantId']
if response.status_code == ExpectedCode1:
    result19 = 'PASS'
else:
    result19 = 'FAIL'


# Post Save entity setup
print("Save entity setup")
parameters = {'daysToWaitForDisbursement': defaultNumberOfDaysForDisbursement,
              'defaultPayType': paymentType,
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + entity_ID + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Status code: {}'.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result20 = 'PASS'
else:
    result20 = 'FAIL'


# Get particular entity setup
print("Get particular entity setup")
response = requests.get(url + 'entities/' + entity_ID + entity_setup, headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result21 = 'PASS'
else:
    result21 = 'FAIL'


# Payments

# GET all payments for particular entity
print("GET all payments for particular entity")
response = requests.get(url + 'entities/' + entity_ID + Payments, headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
paymentNumber1 = data['result'][3]["paymentNumber"]
paymentNumber2 = data['result'][4]["paymentNumber"]
paymentNumber3 = data['result'][5]["paymentNumber"]
paymentNumber4 = data['result'][6]["paymentNumber"]
transactionNumber = data['result'][3]["transactionNumber"]
vendorName = data['result'][3]["payeeName"]
if response.status_code == ExpectedCode1:
    result22 = 'PASS'
else:
    result22 = 'FAIL'


# GET a particular payment's details of a particular entity
print("GET a particular payment's details of a particular entity")
response = requests.get(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber1, headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result23 = 'PASS'
else:
    result23 = 'FAIL'


# Update Payment Status for Batch Payment
print("Update Payment Status for Batch Payment")
parameters = {'paymentFileName': 'paymentFileName' + str(random_value),
              'status': 1}
response = requests.get(url + 'entities/' + entity_ID + '/' + payment_status, data=json.dumps(parameters),
                        headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result24 = 'PASS'
else:
    result24 = 'FAIL'

# GET payments based on search filter : paymentStatus
print("GET payments based on search filter: paymentStatus")
parameters = {'paymentStatus': [paymentStatus]}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result25 = 'PASS'
else:
    result25 = 'FAIL'


# GET payments based on search filter: vendor Name
print("GET payments based on search filter")
parameters = {'vendorName': vendorName}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result26 = 'PASS'
else:
    result26 = 'FAIL'

# GET payments based on search filter: paymentType
print("GET payments based on search filter")
parameters = {'paymentType': paymentType}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result27 = 'PASS'
else:
    result27 = 'FAIL'

# GET payments based on search filter: transactionNumber
print("GET payments based on search filter : transactionNumber")
parameters = {'transactionNumber': transactionNumber}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result28 = 'PASS'
else:
    result28 = 'FAIL'

# GET payments based on search filter: paymentDates
print("GET payments based on search filter : paymentDates")
parameters = {'paymentStartDate': start_date,
              'paymentEndDate': end_date}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result29 = 'PASS'
else:
    result29 = 'FAIL'

# GET payments based on search filter: ClearedDates
print("GET payments based on search filter : ClearedDates")
parameters = {'clearedDateStart': start_date,
              'clearedDateEnd': end_date}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result30 = 'PASS'
else:
    result30 = 'FAIL'


# POST  Retry payment
print("POST Update Retry for payment")
parameters = {
  "paymentType": Paytype_ACH
}
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber3 + Retry_Payments, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result31 = 'PASS'
else:
    result31 = 'FAIL'



# POST  Refund payment
print("POST Refund for payment")
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber4 + Refund_Payments,
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result32 = 'PASS'
else:
    result32 = 'FAIL'


# Remove SFTP Credentials for Company Setup
print("Remove SFTP Credentials for Company Setup")
response = requests.delete(url + remove_credentials, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result33 = 'PASS'
else:
    result33 = 'FAIL'