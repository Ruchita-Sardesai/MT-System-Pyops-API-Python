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

# BATCHES

# Add Batch Transmission Payments into Mineral tree
print("Add Batch Transmission Payments into Mineral tree")
parameters = {
    "batchNumber": 601,
    "amount": 100,
    "tenantId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "payments": [
        {
            "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "batchId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "batchNumber": 0,
            "tenantId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "erpBatchNumber": "string",
            "paymentNumber": "string",
            "currency": "string",
            "paymentDate": "2021-03-24T12:19:24.558Z",
            "paymentSubmittedDate": "2021-03-24T12:19:24.558Z",
            "amount": 0,
            "clearedDate": "2021-03-24T12:19:24.558Z",
            "clearedAmount": 0,
            "disbursementFileName": "string",
            "paymentType": "string",
            "checkNumber": 0,
            "isDefaultPaymentType": true,
            "status": "UnConfirmed",
            "paymentFlag": "FirstCardPayment",
            "obi": "string",
            "transactionNumber": "string",
            "originatingAccountCode": "string",
            "invoices": [
                {
                    "number": "string",
                    "date": "2021-03-24T12:19:24.558Z",
                    "dueDate": "2021-03-24T12:19:24.558Z",
                    "poNumber": "string",
                    "voucherNumber": "string",
                    "grossAmount": 0,
                    "discountAmount": 0,
                    "netAmount": 0,
                    "description": "string",
                    "originalAmount": 0,
                    "payeeNumber": "string",
                    "paymentNumber": "string",
                    "customField1": "string",
                    "customField2": "string",
                    "customField3": "string",
                    "customField4": "string",
                    "customField5": "string"
                }
            ],
            "isValid": true,
            "payeeNumber": "string",
            "payee": {
                "payeeNumber": "string",
                "name": "string",
                "contactInformation": {
                    "contactName": "string",
                    "contactEmail": "string",
                    "phone": "string"
                },
                "address": {
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "city": "string",
                    "state": "string",
                    "countryCode": "string",
                    "zipCode": "string",
                    "country": "string"
                },
                "bankAccount": {
                    "accountNumber": "string",
                    "iban": "string",
                    "otherAccountNumber": "string",
                    "domesticRoutingCode": "string",
                    "swift": "string",
                    "accountType": "string",
                    "accountCurrency": "string",
                    "bankName": "string",
                    "bankAddress1": "string",
                    "bankAddress2": "string",
                    "bankAddress3": "string",
                    "bankCity": "string",
                    "bankState": "string",
                    "bankZipcode": "string",
                    "bankCountry": "string",
                    "bankCountryCode": "string"
                }
            },
            "payor": {
                "name": "string",
                "address": {
                    "addressLine1": "string",
                    "addressLine2": "string",
                    "addressLine3": "string",
                    "city": "string",
                    "state": "string",
                    "countryCode": "string",
                    "zipCode": "string",
                    "country": "string"
                },
                "bankAccount": {
                    "accountNumber": "string",
                    "iban": "string",
                    "otherAccountNumber": "string",
                    "domesticRoutingCode": "string",
                    "swift": "string",
                    "accountType": "string",
                    "accountCurrency": "string",
                    "bankName": "string",
                    "bankAddress1": "string",
                    "bankAddress2": "string",
                    "bankAddress3": "string",
                    "bankCity": "string",
                    "bankState": "string",
                    "bankZipcode": "string",
                    "bankCountry": "string",
                    "bankCountryCode": "string"
                }
            },
            "customField1": "string",
            "customField2": "string",
            "customField3": "string",
            "customField4": "string",
            "customField5": "string",
            "settlementFileName": "string",
            "refundFileName": "string",
            "settlementTransactionId": "string",
            "ach": {
                "formatCode": "string",
                "secureStorage": true
            },
            "card": {
                "cardType": "SingleUse",
                "validityInDays": 0,
                "secret": "string"
            },
            "wire": {
                "purposeCode": "string"
            },
            "check": {
                "signature": "string",
                "template": "string",
                "deliveryMethod": "string"
            },
            "validationErrors": [
                {
                    "id": "string",
                    "error": "string"
                }
            ],
            "paymentApproverActions": [
                {
                    "id": 0,
                    "approverId": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                    "email": "string",
                    "firstName": "string",
                    "middleName": "string",
                    "lastName": "string",
                    "paymentStatus": "string",
                    "dateTime": "2021-03-24T12:19:24.559Z",
                    "comments": "string",
                    "createdDate": "2021-03-24T12:19:24.559Z",
                    "createdBy": "string",
                    "lastModifiedDate": "2021-03-24T12:19:24.559Z",
                    "lastModifiedBy": "string"
                }
            ]
        }
    ],
    "status": "SettlementFileGenerated",
    "disbursement": "2021-03-24T12:19:24.559Z",
    "batchSubmittedDate": "2021-03-24T12:19:24.559Z",
    "paymentFileName": "string"
}
response = requests.post(url + batch_status, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("1.1 Verify User is NOT able to Add Batch Transmission Payments into Mineral tree with expired token ")
response = requests.post(url + batch_status, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("1.2 Verify User is NOT able to Add Batch Transmission Payments into Mineral tree without permission")
response = requests.post(url + batch_status, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


# GET Batches by Current Date
print("Get Batches by Current Date")
response = requests.get(url + current_date, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("2.1 Verify User is NOT able to Get Batches by Current Date with expired token")
response = requests.get(url + current_date, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("2.1 Verify User is NOT able to Get Batches by Current Date without permission")
response = requests.get(url + current_date, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


#Get Payments for Batch
print("Get Payments for Batch")
response = requests.get(url + batch_payments, data=json.dumps(parameters), headers=headers, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("3.1 Verify User is NOT able to Get Payments for Batch with expired token")
response = requests.get(url + batch_payments, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("3.1 Verify User is NOT able to Get Payments for Batch without permission")
response = requests.get(url + batch_payments, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


#Update Batch status
print("Update Batch batch status for batch into Mineral tree")
parameters = {
   'paymentFileName': 'PaymentFile' + random_value,
   'status': '1'
}
response = requests.post(url + update_batch, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.1 Verify User is NOT able to Update Batch batch status for batch into Mineral tree with expired token ")
parameters = {
   'paymentFileName': 'PaymentFile' + random_value,
   'status': '1'
}
response = requests.post(url + update_batch, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("4.2 Verify User is NOT able to Update Batch batch status for batch into Mineral tree without permisison")
parameters = {
   'paymentFileName': 'PaymentFile' + random_value,
   'status': '1'
}
response = requests.post(url + update_batch, data=json.dumps(parameters), headers=NoPermission_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))

print("4.2 Verify User is NOT able to Update Batch batch status for batch into Mineral tree without mandatory fields")
parameters = {
   'paymentFileName': '',
   'status': ''
}
response = requests.post(url + update_batch, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))


print("4.3 Verify User is NOT able to Update Batch batch status for batch into Mineral tree with Invalid status")
parameters = {
   'paymentFileName': 'PaymentFile' + random_value,
   'status': Invalid
}
response = requests.post(url + update_batch, data=json.dumps(parameters), headers=expired_header, verify=True)
print('Request body: {} '.format(response.request.body))
print('Request body: {} '.format(response.request.url))
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))