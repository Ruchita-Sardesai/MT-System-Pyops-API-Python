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

# PAYMENTOPS SETUP

# Post Default Setup for Company Account API
print("1.1 Verify user is not able to Post Default Setup for Company Account with expired token")
parameters = {
    'defaultNumberOfDaysForDisbursement': defaultNumberOfDaysForDisbursement,
    'nextCheckNumber': nextCheckNumber,
    'settlementType': settlementType1,
    'defaultPayType': defaultPayType
}
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
parameters = {
    'defaultNumberOfDaysForDisbursement': 0,
    'nextCheckNumber': 0,
    'settlementType': settlementType1,
    'defaultPayType': defaultPayType
}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("1.4 Verify user is not able to Post Default Setup for Company Account with nextCheckNumber 0")
parameters = {
    'defaultNumberOfDaysForDisbursement': 10,
    'nextCheckNumber': 0,
    'settlementType': settlementType1,
    'defaultPayType': defaultPayType
}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("1.5 Verify user is not able to Post Default Setup for Company Account with invalid settlementType")
parameters = {
    'defaultNumberOfDaysForDisbursement': 10,
    'nextCheckNumber': 2,
    'settlementType': 'Invalid',
    'defaultPayType': defaultPayType
}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print(
    "1.6 Verify user is not able to Post Default Setup for Company Account with nextCheckNumber less than the current check number")
parameters = {
    'defaultNumberOfDaysForDisbursement': 10,
    'nextCheckNumber': 2,
    'settlementType': settlementType1,
    'defaultPayType': defaultPayType
}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("1.7 Verify user is not able to Post Default Setup for Company Account with Invalid defaultpaytype")
parameters = {
    'defaultNumberOfDaysForDisbursement': 10,
    'nextCheckNumber': 2,
    'settlementType': settlementType1,
    'defaultPayType': Invalid
}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("1.8 Verify user is not able to Post Default Setup for Company Account with empty defaultpaytype")
parameters = {
    'defaultNumberOfDaysForDisbursement': 10,
    'nextCheckNumber': 2,
    'settlementType': settlementType1,
    'defaultPayType': ''
}
response = requests.post(url + default_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

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
parameters = {'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': countryCode,
              'zipCode': zipCode,
              'country': country}
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

# Add Card-account for Company Account
print("3.1 Verify user is not able to Add Card-account for Payment_ops Company Account with expired token.")
parameters = {
    'companyNumber': compNumber,
    'fundingAlias': fundingAlias,
    'defaultCardValidity': defaultCardValidity,
    'cardType': cardType
}
response = requests.post(url + card_account, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print(
    "3.2 Verify User without proper permission is not able to Add Card-account for Payment_ops Company Account")
response = requests.post(url + card_account, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("3.3 Verify user is not able to Add Card-account for Payment_ops Company Account without mandatory fields.")
parameters = {
    'companyNumber': '',
    'fundingAlias': '',
    'defaultCardValidity': 12,
    'cardType': ''
}
response = requests.post(url + card_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("3.4 Verify user is not able to Add Card-account for Payment_ops Company Account with defaultCardValidity 0.")
parameters = {
    'companyNumber': compNumber,
    'fundingAlias': fundingAlias,
    'defaultCardValidity': 0,
    'cardType': cardType
}
response = requests.post(url + card_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("3.5 Verify user is not able to Add Card-account for Payment_ops Company Account with invalid cardType.")
parameters = {
    'companyNumber': compNumber,
    'fundingAlias': fundingAlias,
    'defaultCardValidity': defaultCardValidity,
    'cardType': Invalid
}
response = requests.post(url + card_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

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

# Add Check-account for Company Account
print("4.1 Verify user is not able to Add check-account for Payment_ops Company Account with expired token.")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
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
response = requests.post(url + check_account, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))

print("4.2 Verify User without proper permission is not able to Add check-account for Payment_ops Company Account.")
response = requests.post(url + check_account, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.3 Verify user is not able to Add check-account for Payment_ops Company Account without mandatory fields.")
parameters = {'defaultMailingCodeType': '',
              'defaultHandlingCodeType': '',
              'checkFileName': '',
              'addressName': '',
              'addressLine1': '',
              'addressLine2': '',
              'addressLine3': '',
              'city': '',
              'state': '',
              'countryCode': '',
              'zipCode': '',
              'country': ''
              }
response = requests.post(url + check_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.4 Verify user is not able to Add check-account for Payment_ops Company Account with invalid Zipcode.")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
              'addressName': ReturnToName,
              'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': countryCode,
              'zipCode': '123456',
              'country': country
              }
response = requests.post(url + check_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.5 Verify user is not able to Add check-account for Payment_ops Company Account with invalid Country Code.")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
              'addressName': ReturnToName,
              'addressLine1': addressLine1,
              'addressLine2': addressLine2,
              'addressLine3': addressLine3,
              'city': city,
              'state': state,
              'countryCode': 'USA',
              'zipCode': zipCode,
              'country': country
              }
response = requests.post(url + check_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.6 Verify user is not able to Add check-account for Payment_ops Company Account with invalid defaultMailingCodeType.")
parameters = {'defaultMailingCodeType': Invalid,
              'defaultHandlingCodeType': defaultHandlingCodeType,
              'checkFileName': checkFileName,
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
response = requests.post(url + check_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.7 Verify user is not able to Add check-account for Payment_ops Company Account with invalid defaultHandlingCodeType.")
parameters = {'defaultMailingCodeType': defaultMailingCodeType,
              'defaultHandlingCodeType': Invalid,
              'checkFileName': checkFileName,
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
response = requests.post(url + check_account, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

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
response = requests.post(url + check_account, data=json.dumps(parameters),headers=headers, verify=True)
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
response = requests.post(url + ach_account, data=json.dumps(parameters), headers=expired_header, verify=True)
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
response = requests.post(url + ach_account, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
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


# View setup details for a Company Account
print("6.1 Verify user is not able to View setup details for a Company Account with expired token")
response = requests.get(url + setup, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("6.2 Verify User without proper permission is not able to View setup details for a Company Account.")
response = requests.get(url + setup, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# View setup details for a Company Account
print("View setup details for a Company Account")
response = requests.get(url + setup, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))



# Get next_check_number from a default Company Account
print("7.1 Verify user is not able to Get next_check_number form a default Company Account with expired token")
response = requests.get(url + next_check_number, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("7.2 Verify User without proper permission is not able to Get next_check_number form a default Company Account.")
response = requests.get(url + next_check_number, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("Get next_check_number form a default Company Account")
response = requests.get(url + next_check_number, headers=headers, verify=True)
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

print("Get next_Batch_number form a default Company Account")
response = requests.get(url + next_batch_number, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))




# Get next_settlement_transaction_id form a default Company Account
print("9.1 Get next_settlement_transaction_id from a default Company Account with expired token")
response = requests.get(url + next_settlement_transaction_id, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("9.2 Verify User without proper permission is not able to Get next_settlement_transaction_id from a default Company Account with expired token")
response = requests.get(url + next_settlement_transaction_id, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("Get next_settlement_transaction_id form a default Company Account")
response = requests.get(url + next_settlement_transaction_id, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


#SFTP

# Remove SFTP Credentials for Company Setup
print("10.1 Verify user is not able to Remove SFTP Credentials for Company Setup with expired token")
response = requests.post(url + remove_credentials, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("10.2 Verify User without proper permission is not able to Remove SFTP Credentials for Company Setup")
response = requests.post(url + remove_credentials, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("Remove SFTP Credentials for Company Setup")
response = requests.delete(url + remove_credentials, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


# Api to add sftp for setup with PrivateKey authenticationType1.
print("10.3 Verify user is not able to Add SFTP Credentials for Company Setup with expired token")
parameters = {'username': username,
              'password': password,
              'credentialName': credentialName}
response = requests.post(url + add_credentials, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("10.4 Verify User without proper permission is not able to Add SFTP Credentials for Company Setup")
response = requests.post(url + add_credentials, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("10.5 Verify user is not able to Add SFTP Credentials for Company Setup without mandatory fields")
parameters = {'username': '',
              'password': '',
              'credentialName': ''}
response = requests.post(url + add_credentials, data=json.dumps(parameters),headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("10.12 Verify User NOT able to add sftp for setup with PrivateKey authenticationType with expired token.")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType1}
response = requests.post(url + sftp, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("10.13 Verify User NOT able to add sftp for setup with PrivateKey authenticationType without proper permisison")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType1}
response = requests.post(url + sftp, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("10.14 Verify User NOT able to add sftp for setup with PrivateKey authenticationType without mandatory fields.")
parameters = {'host': '',
              'port': '',
              'authenticationType': ''}
response = requests.post(url + sftp, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))



print("Api to add sftp for setup with PrivateKey authenticationType1.")
parameters = {'host': host,
              'port': port,
              'authenticationType': authenticationType1}
response = requests.post(url + sftp, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


# Generate SSH key pairs
print(" 10.6 Verify User is NOT able to Generate SSH key pairs with expired token")
parameters = {'privateKeyName': privateKeyName}
response = requests.post(url + sftp_shh, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("10.7 Verify User is NOT able to Generate SSH key pairs without proper permission")
parameters = {'privateKeyName': privateKeyName}
response = requests.post(url + sftp_shh, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("Generate SSH key pairs")
parameters = {'privateKeyName': privateKeyName}
response = requests.post(url + sftp_shh, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


# Get Public SSH Key
print("10.8 Verify User is NOT able to Get Public SSH Key without proper permission")
response = requests.get(url + sftp_shh_public_key, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("10.9 Verify User is NOT able to Get Public SSH Key with expired token")
response = requests.get(url + sftp_shh_public_key, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("Get Public SSH Key")
response = requests.get(url + sftp_shh_public_key, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


# Remove SSH Keys
print("10.10 Verify User is NOT able to Remove SSH Keys with expired token")
response = requests.delete(url + sftp_shh, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("10.11 Verify User is NOT able to Remove SSH Keys without proper permission")
response = requests.delete(url + sftp_shh, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("Remove SSH Keys")
response = requests.delete(url + sftp_shh, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


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


# Test SFTP Connection for Company Setup
print("11.1 Verify user is not able to Test SFTP Connection for Company Setup with expired token")
response = requests.post(url + test_connections, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))

print("11.2 Verify User without proper permission is not able to Test SFTP Connection for Company Setup")
response = requests.post(url + test_connections, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("Test SFTP Connection for Company Setup")
response = requests.post(url + test_connections, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))



# Add file location for SFTP
print("12.1 Verify User NOT able to Add file location for SFTP with expired token")
parameters = {'checkFileLocation': checkFileLocation,
              'achFileLocation': achFileLocation,
              'cardFileLocation': cardFileLocation}
response = requests.post(url + file_location, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("12.2 Verify User NOT able to Add file location for SFTP without proper permission")
parameters = {'checkFileLocation': checkFileLocation,
              'achFileLocation': achFileLocation,
              'cardFileLocation': cardFileLocation}
response = requests.post(url + file_location, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("12.2 Verify User NOT able to Add file location for SFTP without Mandatory fields")
parameters = {'checkFileLocation': '',
              'achFileLocation': '',
              'cardFileLocation': ''}
response = requests.post(url + file_location, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("Add file location for SFTP")
parameters = {'checkFileLocation': checkFileLocation,
              'achFileLocation': achFileLocation,
              'cardFileLocation': cardFileLocation}
response = requests.post(url + file_location, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

# ENTITIES

# Get Entities for Applications
print("13.1 Verify User is NOT able to Get Entities for Applications with expired token")
response = requests.get(url + entities, headers=expired_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("13.2 Verify User is NOT able to Get Entities for Applications without permisison")
response = requests.get(url + entities, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("Get Entities for Applications")
response = requests.get(url + entities, headers=headers, verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))



# Get All entity setups
print("14.1 Verify User is NOT able to Get All entity setups with expired token")
response = requests.get(url + entity_setups, headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("14.2 Verify User is NOT able to Get All entity setups without permission")
response = requests.get(url + entity_setups, headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("Get All entity setups")
response = requests.get(url + entity_setups, headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
data = json.loads(response.content)
entity_ID = data['result'][2]['tenantId']


# Post Save entity setup
print("15.1 Verify User is NOT able to Save entity setup with expired token")
parameters = {'daysToWaitForDisbursement': defaultNumberOfDaysForDisbursement,
              'defaultPayType': paymentType,
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + entity_ID + entity_setup, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Status code: {}'.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("15.2 Verify User is NOT able to Save entity setup without permission")
parameters = {'daysToWaitForDisbursement': defaultNumberOfDaysForDisbursement,
              'defaultPayType': paymentType,
              'settlementType': settlementType1}
response = requests.post(url + 'entities/' + entity_ID + entity_setup, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("15.3 Verify User is NOT able to Save entity setup without Mandatory fields")
parameters = {'daysToWaitForDisbursement': '',
              'defaultPayType': '',
              'settlementType': ''}
response = requests.post(url + 'entities/' + entity_ID + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Status code: {}'.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("15.4 Verify User is NOT able to Save entity setup with Invalid fields")
parameters = {'daysToWaitForDisbursement': Invalid,
              'defaultPayType': Invalid,
              'settlementType': Invalid}
response = requests.post(url + 'entities/' + entity_ID + entity_setup, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Status code: {}'.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


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


# Get a particular entity setup
print("16.1 Verify user is not able to Get a particular entity setup with expired token")
response = requests.get(url + 'entities/' + entity_ID + entity_setup, headers=expired_header, verify=True)
print('Status code: {}'.format(response.request.url))
print('Status code: {}'.format(response.status_code))

print("16.2 Verify User without proper permission is not able to Get a particular entity setup")
response = requests.get(url + 'entities/' + entity_ID + entity_setup, headers=NoPermission_header, verify=True)
print('Status code: {}'.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("16.3 Verify User is not able to Get a particular entity setup when EntityID is not proper")
response = requests.get(url + 'entities/' + Invalid + entity_setup, headers=headers, verify=True)
print('Status code: {}'.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))



# PAYMENTS

# GET all payments for particular entity
print("17.1 Verify User Is NOT able to GET all payments for particular entity with expired token")
response = requests.get(url + 'entities/' + entity_ID + Payments, headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("17.2 Verify User Is NOT able to GET all payments for particular entity without permission")
response = requests.get(url + 'entities/' + entity_ID + Payments, headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


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



# GET a particular payment's details of a particular entity
print("18.1 Verify User is NOT able to GET a particular payment's details of a particular entity with expired token")
response = requests.get(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber1, headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("18.2 Verify User is NOT able to GET a particular payment's details of a particular entity without permission")
response = requests.get(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber1, headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("GET a particular payment's details of a particular entity")
response = requests.get(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber1, headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


# Update Payment Status for Batch Payment
print("19.1 Verify User is NOT able to Update Payment Status for Batch Payment with expired token")
parameters = {'paymentFileName': 'paymentFileName' + str(random_value),
              'status': 1}
response = requests.get(url + 'entities/' + entity_ID + '/' + payment_status, data=json.dumps(parameters),
                        headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("19.2 Verify User is NOT able to Update Payment Status for Batch Payment without permission")
parameters = {'paymentFileName': 'paymentFileName' + str(random_value),
              'status': 1}
response = requests.get(url + 'entities/' + entity_ID + '/' + payment_status, data=json.dumps(parameters),
                        headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("19.3 Verify User is NOT able to Update Payment Status for Batch Payment without mandatory fields")
parameters = {'paymentFileName': '',
              'status': ''}
response = requests.get(url + 'entities/' + entity_ID + '/' + payment_status, data=json.dumps(parameters),
                        headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("19.4 Verify User is NOT able to Update Payment Status for Batch Payment with Invalid fields")
parameters = {'paymentFileName': 'paymentFileName' + str(random_value),
              'status': Invalid}
response = requests.get(url + 'entities/' + entity_ID + '/' + payment_status, data=json.dumps(parameters),
                        headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("Update Payment Status for Batch Payment")
parameters = {'paymentFileName': 'paymentFileName' + str(random_value),
              'status': 1}
response = requests.get(url + 'entities/' + entity_ID + '/' + payment_status, data=json.dumps(parameters),
                        headers=headers, verify=True)
print('Request body: {} '.format(response.request.url))
print('Request body: {} '.format(response.request.body))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))




# GET payments based on search filter
print("20.1 Verify User is NOT able to GET payments based on search filter with expired token")
parameters = {'paymentStatus': [paymentStatus]}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("20.2 Verify User is NOT able to GET payments based on search filter without permission")
parameters = {'paymentStatus': [paymentStatus]}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("GET payments based on search filter: paymentStatus")
parameters = {'paymentStatus': [paymentStatus]}
response = requests.post(url + 'entities/' + entity_ID + Payments + Payment_search, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


# POST  Retry payment
print("21.1 Verify User is NOT able to POST Update Retry for payment with expired token")
parameters = {
  "paymentType": Paytype_ACH
}
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber3 + Retry_Payments, data=json.dumps(parameters),
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))


print("21.2 Verify User is NOT able to POST Update Retry for payment without permission")
parameters = {
  "paymentType": Paytype_ACH
}
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber3 + Retry_Payments, data=json.dumps(parameters),
                         headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))


print("21.3 Verify User is NOT able to POST Update Retry for payment with Invalid paymenttype")
parameters = {
  "paymentType": Invalid
}
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber3 + Retry_Payments, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))


print("21.4 Verify User is NOT able to POST Update Retry for payment without paymenttype")
parameters = {
  "paymentType": ''
}
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber3 + Retry_Payments, data=json.dumps(parameters),
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))


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


# POST  Refund payment
print("22.1 Verify User is NOT able to POST Refund for payment with expired token")
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber4 + Refund_Payments,
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("22.2 Verify User is NOT able to POST Refund for payment without permission")
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber4 + Refund_Payments,
                         headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("22.3 Verify User is NOT able to POST Refund for payment with Invalid payment number")
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + Invalid + Refund_Payments,
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("POST Refund for payment")
response = requests.post(url + 'entities/' + entity_ID + Payments + '/' + paymentNumber4 + Refund_Payments,
                         headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
