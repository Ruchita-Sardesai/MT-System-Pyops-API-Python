import json
import requests
# import sys

# sys.stdout = open('D:\Project\kote.txt', 'w')

from Generic import *

# Populate Access Token
data = {'grant_type': grant_type, 'username': Username, 'password': Password, 'scope': Scope}
data1 = {'grant_type': grant_type, 'username': InvalidUsername, 'password': InvalidPassword, 'scope': Scope}

# Get access token
access_token_response = requests.post(token_url, data=data, verify=True, allow_redirects=True,
                                      auth=(client_id, client_secret))
NoPermission_header = requests.post(token_url, data=data1, verify=True, allow_redirects=True,
                                    auth=(client_id, client_secret))

# Print access token
print(access_token_response.text)
tokens = json.loads(access_token_response.text)
tokens_np = json.loads(NoPermission_header.text)

headers = {'Authorization': 'Bearer ' + tokens['access_token'], 'Content-Type': 'application/json',
           'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

expired_header = {'Authorization': 'Bearer ' + ExpiredToken, 'Content-Type': 'application/json',
                  'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

NoPermission_header = {'Authorization': 'Bearer ' + tokens_np['access_token'], 'Content-Type': 'application/json',
                       'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

# Post Default Setup for Company Account API
print("1.1 Verify user is not able to Post Default Setup for Company Account with expired token")
parameters = {'defaultNumberOfDaysForDisbursement': defaultNumberOfDaysForDisbursement,
              'nextCheckNumber': nextCheckNumber,
              'settlementType': settlementType1}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("1.2 Verify User without proper permission is not able to Post Default Setup for Company Account")
response = requests.post(url + default_setup, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("1.3 Verify user is not able to Post Default Setup for Company Account with defaultNumberOfDaysForDisbursement 0")
parameters = {'defaultNumberOfDaysForDisbursement': 0,
              'nextCheckNumber': 11,
              'settlementType': settlementType1}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("1.4 Verify user is not able to Post Default Setup for Company Account with nextCheckNumber 0")
parameters = {'defaultNumberOfDaysForDisbursement': 10,
              'nextCheckNumber': 0,
              'settlementType': settlementType1}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("1.5 Verify user is not able to Post Default Setup for Company Account with invalid settlementType")
parameters = {'defaultNumberOfDaysForDisbursement': 10,
              'nextCheckNumber': 2,
              'settlementType': 'Invalid'}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print(
    "1.5 Verify user is not able to Post Default Setup for Company Account with nextCheckNumber less than the current check number")
parameters = {'defaultNumberOfDaysForDisbursement': 10,
              'nextCheckNumber': 2,
              'settlementType': settlementType1}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Add Address for Company Account API
print("2.1 Verify user is not able to Add Address for a Company Account with expired token")
parameters = {'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': countryCode,
              'zipCode': zipCode,
              'country': country}
response = requests.post(url + company_address, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("2.2 Verify User without proper permission is not able to Add Address for a Company Account")
response = requests.post(url + company_address, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("2.3 Verify user is not able to Add Address for a Company Account without mandatory fields")
parameters = {'addressLine1': '',
              'addressLine2': '',
              'addressLine3': '',
              'city': '',
              'state': '',
              'countryCode': '',
              'zipCode': '',
              'country': ''}
response = requests.post(url + company_address, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("2.4 Verify user is not able to Add Address for a Company Account with Zip code more than 5 digits characters")
parameters = {'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': countryCode,
              'zipCode': '123456789',
              'country': country}
response = requests.post(url + company_address, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("2.5 Verify user is not able to Add Address for a Company Account with Country code more than two characters")
parameters = {'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': 'USA',
              'zipCode': zipCode,
              'country': country}
response = requests.post(url + company_address, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Add Card-account for Company Account
print("3.1 Verify user is not able to Add Card-account for Payment_ops Company Account with expired token.")
parameters = {'fundingAlias': fundingAlias,
              'defaultCardValidity': defaultCardValidity,
              'cardType': cardType}
response = requests.post(url + card_account, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print(
    "3.2 Verify User without proper permission is not able to Add Card-account for Payment_ops Company Account with expired token.")
response = requests.post(url + card_account, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("3.3 Verify user is not able to Add Card-account for Payment_ops Company Account without mandatory fields.")
parameters = {'fundingAlias': '',
              'defaultCardValidity': 0,
              'cardType': ''}
response = requests.post(url + card_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("3.4 Verify user is not able to Add Card-account for Payment_ops Company Account with defaultCardValidity 0.")
parameters = {'fundingAlias': fundingAlias,
              'defaultCardValidity': 0,
              'cardType': cardType}
response = requests.post(url + card_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("3.5 Verify user is not able to Add Card-account for Payment_ops Company Account with invalid cardType.")
parameters = {'fundingAlias': fundingAlias,
              'defaultCardValidity': 1,
              'cardType': 'Invalid'}
response = requests.post(url + card_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Add Check-account for Company Account
print("4.1 Verify user is not able to Add check-account for Payment_ops Company Account with expired token.")
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
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("4.2 Verify User without proper permission is not able to Add check-account for Payment_ops Company Account.")
response = requests.post(url + check_account, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.3 Verify user is not able to Add check-account for Payment_ops Company Account without mandatory fields.")
parameters = {'defaultMailingCodeType': '',
              'defaultHandlingCodeType': '',
              'checkFileName': '',
              'addressLine1': '',
              'addressLine2': '',
              'addressLine3': '',
              'city': '',
              'state': '',
              'countryCode': '',
              'zipCode': '',
              'country': ''
              }
response = requests.post(url + check_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.4 Verify user is not able to Add check-account for Payment_ops Company Account with invalid Zipcode.")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
              'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': countryCode,
              'zipCode': '123456',
              'country': country
              }
response = requests.post(url + check_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.5 Verify user is not able to Add check-account for Payment_ops Company Account with invalid Country Code.")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
              'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': 'USA',
              'zipCode': zipCode,
              'country': country
              }
response = requests.post(url + check_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print(
    "4.6 Verify user is not able to Add check-account for Payment_ops Company Account with invalid defaultMailingCodeType.")
parameters = {'defaultMailingCodeType': 'defaultMailingCodeType',
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

print(
    "4.7 Verify user is not able to Add check-account for Payment_ops Company Account with invalid defaultHandlingCodeType.")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': 'defaultHandlingCodeType',
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

# Add ACH-account for Company Account
print("5.1 Verify user is not able to Add ACH-account for Payment_ops Company Account with expired token.")
parameters = {'fileName': fileName,
              'immediateDestination': immediateDestination,
              'immediateDestinationName': immediateDestinationName,
              'immediateOrigin': immediateOrigin,
              'immediateOriginName': immediateOriginName,
              'companyId': companyId,
              'formatCode': formatCode}
response = requests.post(url + ach_account, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("5.2 Verify User without proper permission is not able to Add ACH-account for Payment_ops Company Account")
parameters = {'fileName': fileName,
              'immediateDestination': immediateDestination,
              'immediateDestinationName': immediateDestinationName,
              'immediateOrigin': immediateOrigin,
              'immediateOriginName': immediateOriginName,
              'companyId': companyId,
              'formatCode': formatCode}
response = requests.post(url + ach_account, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("5.3 Verify user is not able to Add ACH-account for Payment_ops Company Account without mandatory fields.")
parameters = {'fileName': '',
              'immediateDestination': '',
              'immediateDestinationName': '',
              'immediateOrigin': '',
              'immediateOriginName': '',
              'companyId': '',
              'formatCode': ''}
response = requests.post(url + ach_account, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# View setup details for a Company Account
print("6.1 Verify user is not able to View setup details for a Company Account with expired token")
response = requests.get(url + setup, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("6.2 Verify User without proper permission is not able to View setup details for a Company Account.")
response = requests.get(url + setup, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Get next_check_number form a default Company Account
print("7.1 Verify user is not able to Get next_check_number form a default Company Account with expired token")
response = requests.get(url + next_check_number, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("7.2 Verify User without proper permission is not able to Get next_check_number form a default Company Account.")
response = requests.get(url + next_check_number, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Get next_Batch_number form a default Company Account
print("8.1 Verify user is not able to Get next_Batch_number form a default Company Account with expired token")
response = requests.get(url + last_batch, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("8.2 Verify User without proper permission is not able to Get next_Batch_number form a default Company Account.")
response = requests.get(url + last_batch, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Get All entities
response = requests.get(url + 'entities', headers=headers, verify=True)
data = json.loads(response.content)
extracted_id = data['result'][1]['id']

print("9.1 Verify user is not able to Get all entities with expired token")
response = requests.get(url + 'entities', headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("9.2 Verify User without proper permission is not able to Get all entities.")
response = requests.get(url + 'entities', headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Get all entities setup
print("10.1 Verify user is not able to Get all entities setup with expired token")
response = requests.get(url + 'entity-setups', headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))

print("10.2 Verify User without proper permission is not able to Get all entities setup.")
response = requests.get(url + 'entity-setups', headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Post a particular entity setup
print("11.1 Verify user is not able to Save a particular entity setup with expired token")
parameters = {'daysToWaitForDisbursement': daysToWaitForDisbursement,
              'defaultPayType': defaultPayType,
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("11.2 Verify User without proper permission is not able to Save a particular entity setup")
parameters = {'daysToWaitForDisbursement': daysToWaitForDisbursement,
              'defaultPayType': defaultPayType,
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("11.3 Verify user is able to Save a particular entity setup with daysToWaitForDisbursement 0")
parameters = {'daysToWaitForDisbursement': 0,
              'defaultPayType': defaultPayType,
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("11.4 Verify user is not able to Save a particular entity setup without defaultPayType")
parameters = {'daysToWaitForDisbursement': 10,
              'defaultPayType': '',
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("11.4 Verify user is not able to Save a particular entity setup Invalid defaultPayType")
parameters = {'daysToWaitForDisbursement': 10,
              'defaultPayType': 'invalid',
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("11.5 Verify user is not able to Save a particular entity setup without settlementType")
parameters = {'daysToWaitForDisbursement': 10,
              'defaultPayType': defaultPayType,
              'settlementType': ''}
response = requests.post(url + 'entities/' + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("11.6 Verify user is not able to Save a particular entity setup with invalid settlementType")
parameters = {'daysToWaitForDisbursement': 10,
              'defaultPayType': '',
              'settlementType': 'invalid'}
response = requests.post(url + 'entities/' + extracted_id + '/' + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Get a particular entity setup
print("12.1 Verify user is not able to Get a particular entity setup with expired token")
response = requests.get(url + 'entities/' + extracted_id + '/' + entity_setup, headers=expired_header, verify=True)
print('Status code: {}'.format(response.request.url))
print('Status code: {}'.format(response.status_code))

print("12.2 Verify User without proper permission is not able to Get a particular entity setup")
response = requests.get(url + 'entities/' + extracted_id + '/' + entity_setup,
                        headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("12.3 Verify User is not able to Get a particular entity setup when EntityID is not proper")
response = requests.get(url + 'entities/' + InvalidTenant_ID + '/' + entity_setup, headers=headers, verify=True)
print('Status code: {}'.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Remove SFTP Credentials for Company Setup
print("13.1 Verify user is not able to Remove SFTP Credentials for Company Setup with expired token")
response = requests.post(url + remove_credentials, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("13.2 Verify User without proper permission is not able to Remove SFTP Credentials for Company Setup")
response = requests.post(url + remove_credentials, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Add SFTP Credentials for Company Setup
print("14.1 Verify user is not able to Add SFTP Credentials for Company Setup with expired token")
parameters = {'username': username,
              'password': password,
              'credentialName': credentialName,
              'authenticationType': authenticationType}
response = requests.post(url + add_credentials, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("14.2 Verify User without proper permission is not able to Add SFTP Credentials for Company Setup")
response = requests.post(url + add_credentials, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("14.3 Verify user is not able to Add SFTP Credentials for Company Setup without mandatory fields")
parameters = {'username': '',
              'password': '',
              'credentialName': '',
              'authenticationType': ''}
response = requests.post(url + add_credentials, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Test SFTP Connection for Company Setup
print("15.1 Verify user is not able to Test SFTP Connection for Company Setup with expired token")
response = requests.post(url + test_connections, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("15.2 Verify User without proper permission is not able to Test SFTP Connection for Company Setup")
response = requests.post(url + test_connections, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Remove SSH Keys
print("16.1 Verify user is not able to Remove SSH Keys for Company Setup with expired token")
response = requests.delete(url + sftp_shh, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("16.2 Verify User without proper permission is not able to Remove SSH Keys for Company Setup")
response = requests.post(url + test_connections, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Remove SSH Keys
print("16.1 Verify user is not able to Remove SSH Keys for Company Setup with expired token")
response = requests.delete(url + sftp_shh, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("16.2 Verify User without proper permission is not able to Remove SSH Keys for Company Setup")
response = requests.post(url + test_connections, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Add file location for SFTP
print("17.1 Verify user is not able to Add file location for SFTP with expired token")
parameters = {'checkFileLocation': checkFileLocation,
              'achFileLocation': achFileLocation,
              'cardFileLocation': cardFileLocation}
response = requests.post(url + file_location, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("17.2 Verify User without proper permission is not able to Add file location for SFTP")
response = requests.post(url + file_location, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("17.3 Verify mandatory field validations for Add file location for SFTP")
parameters = {'checkFileLocation': '',
              'achFileLocation': '',
              'cardFileLocation': ''}
response = requests.post(url + file_location, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Generate SSH key pairs
print("18.1 Verify user is not able to Generate SSH key pairs with expired token")
parameters = {'privateKeyName': privateKeyName}
response = requests.post(url + sftp_shh, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("18.2 Verify User without proper permission is not able to Generate SSH key pairs")
parameters = {'privateKeyName': privateKeyName}
response = requests.post(url + sftp_shh, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("18.3 Verify mandatory field validations for Generate SSH key pairs")
parameters = {'privateKeyName': ''}
response = requests.post(url + sftp_shh, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Api to add sftp for setup.
print("19.1 Verify user is not able to add sftp for setup. with expired token")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType}
response = requests.post(url + sftp, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("19.2 Verify User without proper permission is not able to add sftp for setup.")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType}
response = requests.post(url + sftp, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("19.3 Verify mandatory field validations for add sftp for setup.")
parameters = {'host': '',
              'port': 0,
              'authenticationType': ''}
response = requests.post(url + sftp, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("19.4 Verify validation for invalid authenticationType to add sftp for setup.")
parameters = {'host': host,
              'port': port,
              'authenticationType': 'authenticationType'}
response = requests.post(url + sftp, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("19.5 Verify validation for invalid host to add sftp for setup.")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType}
response = requests.post(url + sftp, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# Get Public SSH Key
print("20.1 Verify user is not able to Get Public SSH Key with expired token")
response = requests.get(url + sftp_shh_public_key, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("20.2 Verify User without proper permission is not able to Get Public SSH Key")
response = requests.get(url + sftp_shh_public_key, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# GET all payments for particular entity
print("21.1 Verify user is not able to GET all payments for particular entity with expired token")
response = requests.get(url + Payments, headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print(
    "21.2 Verify User without proper permission is not able to GET a particular payment's details of a particular entity")
response = requests.get(url + Payments, headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("21.3 Verify validation for invalid tenantID to GET a particular payment's details of a particular entity")
response = requests.get(url + 'entities/' + InvalidTenant_ID + '/payments', headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# GET a particular payment's details of a particular entity
response = requests.get(url + Payments, headers=headers, verify=True)
data = json.loads(response.content)
extracted_id = data['result'][1]["paymentNumber"]
transactionNumber = data['result'][1]["transactionNumber"]
vendorName = data['result'][1]["payeeName"]

print("22.1 Verify user is not able to GET a particular payment's details of a particular entity with expired token")
response = requests.get(url + Payments + '/' + extracted_id, headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print(
    "22.2 Verify User without proper permission is not able to GET a particular payment's details of a particular entity")
response = requests.get(url + Payments + '/' + extracted_id, headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("22.3 Verify validation with invalid TenantID to GET a particular payment's details of a particular entity")
response = requests.get(url + 'entities/' + InvalidTenant_ID + '/payments/' + extracted_id, headers=headers,
                        verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("22.4 Verify validation with invalid PaymentNo to GET a particular payment's details of a particular entity")
response = requests.get(url + Payments + '/' + '123', headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# GET payments based on search filter: vendor Name
print("23.1 Verify user is not able to GET payments based on search filter with expired token")
parameters = {'vendorName': vendorName}
response = requests.post(url + Payment_search, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))

print("23.2 Verify User without proper permission is not able to GET payments based on search filter")
parameters = {'vendorName': vendorName}
response = requests.post(url + Payment_search, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("23.3 Verify mandatory field validations for GET payments based on search filter")
parameters = {'vendorName': '',
              'paymentStatus': [],
              'paymentType': '',
              'transactionNumber': '',
              'paymentStartDate': '',
              'paymentEndDate': '',
              'clearedDateStart': '',
              'clearedDateEnd': ''
              }
response = requests.post(url + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
