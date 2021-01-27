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

# Post Default Setup for Company Account API
print("Post Default Setup for Company Account.")
parameters = {'defaultNumberOfDaysForDisbursement': defaultNumberOfDaysForDisbursement,
              'nextCheckNumber': nextCheckNumber}

response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result6 = 'PASS'
else:
    result6 = 'FAIL'

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
    result1 = 'PASS'
else:
    result1 = 'FAIL'

# Add Card-account for Company Account
print("Add Card-account for Payment_ops Company Account .")
parameters = {'fundingAlias': fundingAlias,
              'defaultCardValidity': defaultCardValidity,
              'cardType': cardType}
response = requests.post(url + card_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result2 = 'PASS'
else:
    result2 = 'FAIL'

# Add Check-account for Company Account
print("Add check-account for Payment_ops Company Account .")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
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
    result3 = 'PASS'
else:
    result3 = 'FAIL'

# Add ACH-account for Company Account
print("Add ACH-account for Payment_ops Company Account .")
parameters = {'fileName': fileName,
              'immediateDestination': immediateDestination,
              'immediateDestinationName': immediateDestinationName,
              'immediateOrigin': immediateOrigin,
              'immediateOriginName': immediateOriginName,
              'companyId': companyId,
              'formatCode': formatCode}
response = requests.post(url + ach_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result4 = 'PASS'
else:
    result4 = 'FAIL'

# View setup details for a Company Account
print("View setup details for a Company Account")
response = requests.get(url + setup, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result5 = 'PASS'
else:
    result5 = 'FAIL'

# Get next_check_number form a default Company Account
print("Get next_check_number form a default Company Account")
response = requests.get(url + next_check_number, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result7 = 'PASS'
else:
    result7 = 'FAIL'

# Get next_Batch_number form a default Company Account
print("Get next_Batch_number form a default Company Account")
response = requests.get(url + last_batch, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result8 = 'PASS'
else:
    result8 = 'FAIL'

# Get All entities
print("Get all entities")
response = requests.get(url + 'entities', headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
extracted_id = data['result'][1]['id']
if response.status_code == ExpectedCode1:
    result15 = 'PASS'
else:
    result15 = 'FAIL'

# Get all entities setup
print("Get all entities setup")
response = requests.get(url + 'entity-setups', headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result9 = 'PASS'
else:
    result9 = 'FAIL'

# Post a particular entity setup
print("Save a particular entity setup")
parameters = {'daysToWaitForDisbursement': daysToWaitForDisbursement,
              'defaultPayType': defaultPayType}
response = requests.post(url + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Status code: {}'.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result11 = 'PASS'
else:
    result11 = 'FAIL'

# Get a particular entity setup
print("Get a particular entity setup")
response = requests.get(url + extracted_id + '/' + entity_setup, headers=headers, verify=True)
print('Status code: {}'.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result10 = 'PASS'
else:
    result10 = 'FAIL'

# Remove SFTP Credentials for Company Setup
print("Remove SFTP Credentials for Company Setup")
response = requests.post(url + remove_credentials, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result13 = 'PASS'
else:
    result13 = 'FAIL'

# Add SFTP Credentials for Company Setup
print("Add SFTP Credentials for Company Setup")
parameters = {'username': username,
              'password': password,
              'credentialName': credentialName,
              'checkFileLocation': checkFileLocation,
              'achFileLocation': achFileLocation,
              'cardFileLocation': cardFileLocation}
response = requests.post(url + add_credentials, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode:
    result12 = 'PASS'
else:
    result12 = 'FAIL'

# Test SFTP Connection for Company Setup
print("Test SFTP Connection for Company Setup")
response = requests.post(url + test_connections, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result14 = 'PASS'
else:
    result14 = 'FAIL'

print("Add Address for Company Account API: " + result1)
print("Add Card-account for Company Account: " + result2)
print("Add Check-account for Company Account: " + result3)
print("Add ACH-account for Company Account: " + result4)
print("View Setup Details: " + result5)
print("Post Default Setup for Company Account API: " + result6)
print("Get next_check_number form a default Company Account: " + result7)
print("Get next_Batch_number form a default Company Account: " + result8)
print("Get all entities setup: " + result9)
print("Get a particular entity setup: " + result10)
print("Save a particular entity setup: " + result11)
print("Add SFTP Credentials for Company Setup: " + result12)
print("Remove SFTP Credentials for Company Setup: " + result13)
print("Test SFTP Connection for Company Setup: " + result14)
print("Get all entities: " + result15)
