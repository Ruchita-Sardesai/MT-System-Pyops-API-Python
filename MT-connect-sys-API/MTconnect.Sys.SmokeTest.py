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



# PaymentsOPS setup

# Post Default Setup for Company Account API
print("Post Default Setup for Company Account.")
parameters = {'defaultNumberOfDaysForDisbursement': defaultNumberOfDaysForDisbursement,
              'nextCheckNumber': nextCheckNumber,
              'settlementType': settlementType1,
              'defaultPayType': defaultPayType}

response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result1 = 'PASS'
else:
    result1 = 'FAIL'

# Add Address for Company Account API
print("Add Address for a Company Account.")
parameters = {'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': countryCode,
              'zipCode': zipCode,
              'country': country}
response = requests.post(url + company_address, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result2 = 'PASS'
else:
    result2 = 'FAIL'

# Add Card-account for Company Account
print("Add Card-account for Payment_ops Company Account .")
parameters = {
              'companyNumber': compNumber,
              'fundingAlias': fundingAlias,
              'defaultCardValidity': defaultCardValidity,
              'cardType': cardType}
response = requests.post(url + card_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result3 = 'PASS'
else:
    result3 = 'FAIL'

# Add Check-account for Company Account
print("Add check-account for Payment_ops Company Account .")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
              'OriginatingAccountNumber': '36925847',
              'addressName': ReturnToName,
              'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': countryCode,
              'zipCode': zipCode,
              'country': country
              }
response = requests.post(url + check_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result4 = 'PASS'
else:
    result4 = 'FAIL'

# Add ACH-account for Company Account
print("Add ACH-account for Payment_ops Company Account .")
parameters = {'fileName': fileName,
              'immediateDestination': immediateDestination,
              'immediateDestinationName': immediateDestinationName,
              'immediateOrigin': immediateOrigin,
              'immediateOriginName': immediateOriginName,
              'companyId': companyId,
              'formatCode': formatCode,
              'originatingDFIId': originatingDFIId}
response = requests.post(url + ach_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result5 = 'PASS'
else:
    result5 = 'FAIL'

# View setup details for a Company Account
print("View setup details for a Company Account")
response = requests.get(url + setup, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result6 = 'PASS'
else:
    result6 = 'FAIL'

# Get next_check_number form a default Company Account
print("Get next_check_number form a default Company Account")
response = requests.get(url + next_check_number, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result7 = 'PASS'
else:
    result7 = 'FAIL'

# Get next_Batch_number from a default Company Account
print("Get next_Batch_number form a default Company Account")
response = requests.get(url + next_batch_number, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result8 = 'PASS'
else:
    result8 = 'FAIL'

# Get next_settlement_transaction_id form a default Company Account
print("Get next_settlement_transaction_id form a default Company Account")
response = requests.get(url + next_settlement_transaction_id, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result9 = 'PASS'
else:
    result9 = 'FAIL'

# SFTP

# Api to add sftp for setup with PrivateKey authenticationType1.
print("Api to add sftp for setup with PrivateKey authenticationType1.")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType1}
response = requests.post(url + sftp, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode:
    result10 = 'PASS'
else:
    result10 = 'FAIL'

# Generate SSH key pairs
print("Generate SSH key pairs")
parameters = {'privateKeyName': privateKeyName}
response = requests.post(url + sftp_shh, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode:
    result11 = 'PASS'
else:
    result11 = 'FAIL'

# Get Public SSH Key
print("Get Public SSH Key")
response = requests.get(url + sftp_shh_public_key, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result12 = 'PASS'
else:
    result12 = 'FAIL'

# Remove SSH Keys
print("Remove SSH Keys")
response = requests.delete(url + sftp_shh, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result13 = 'PASS'
else:
    result13 = 'FAIL'



# Api to add sftp for setup with Password authenticationType2.
print("Api to add sftp for setup with Password authenticationType2.")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType2}
response = requests.post(url + sftp, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode:
    result14 = 'PASS'
else:
    result14 = 'FAIL'

# Add SFTP Credentials for Company Setup
print("Add SFTP Credentials for Company Setup")
parameters = {'username': username,
              'password': password,
              'credentialName': credentialName}
response = requests.post(url + add_credentials, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode:
    result15 = 'PASS'
else:
    result15 = 'FAIL'


# Test SFTP Connection for Company Setup
print("Test SFTP Connection for Company Setup")
response = requests.post(url + test_connections, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result16 = 'PASS'
else:
    result16 = 'FAIL'

# Add file location for SFTP
print("Add file location for SFTP")
parameters = {'checkFileLocation': checkFileLocation,
              'achFileLocation': achFileLocation,
              'cardFileLocation': cardFileLocation}
response = requests.post(url + file_location, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result17 = 'PASS'
else:
    result17 = 'FAIL'


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


# PAYMENTS

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



print("RESULTS:")
print("Post Default Setup for Company Account: " + result1)
print("Add Address for a Company Account: " + result2)
print("Add Card-account for Payment_ops Company Account: " + result3)
print("Add check-account for Payment_ops Company Account: " + result4)
print("Add ACH-account for Payment_ops Company Account: " + result5)
print("View setup details for a Company Account: " + result6)
print("Get next_check_number form a default Company Account: " + result7)
print("Get next_Batch_number form a default Company Account: " + result8)
print("Get next_settlement_transaction_id form a default Company Account: " + result9)
print("Api to add sftp for setup with PrivateKey authenticationType1: " + result10)
print("Generate SSH key pairs: " + result11)
print("Get Public SSH Key: " + result12)
print("Remove SSH Keys: " + result13)
print("Api to add sftp for setup with Password authenticationType2: " + result14)
print("Add SFTP Credentials for Company Setup: " + result15)
print("Test SFTP Connection for Company Setup: " + result16)
print("Add file location for SFTP: " + result17)
print("Get Entities for Applications: " + result18)
print("Get All entity setups: " + result19)
print("Save entity setup: " + result20)
print("Get particular entity setup: " + result21)
print("GET all payments for particular entity: " + result22)
print("GET a particular payment's details of a particular entity: " + result23)
print("Update Payment Status for Batch Payment: " + result24)
print("GET payments based on search filter : paymentStatus: " + result25)
print("GET payments based on search filter: vendor Name: " + result26)
print("GET payments based on search filter: paymentType: " + result27)
print("GET payments based on search filter: transactionNumber: " + result28)
print("GET payments based on search filter: paymentDates: " + result29)
print("GET payments based on search filter: ClearedDates: " + result30)
print("POST  Retry payment: " + result31)
print("POST  Refund payment: " + result32)
print("Remove SFTP Credentials for Company Setup: " + result33)



