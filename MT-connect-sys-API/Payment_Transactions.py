import json
import requests

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

expired_header = {'Authorization': 'Bearer ' + ExpiredToken, 'Content-Type': 'application/json',
                  'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

NoPermission_header = {'Authorization': 'Bearer ' + tokens_np['access_token'], 'Content-Type': 'application/json',
                       'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

# Print access token
print(access_token_response.text)
tokens = json.loads(access_token_response.text)

headers = {'Authorization': 'Bearer ' + tokens['access_token'], 'Content-Type': 'application/json',
           'DataEncoding': 'UTF-8', 'Accept': 'application/json'}

# Get Payment Transactions
print("GET Reports of Payments with report type: SingleTransactionReportType")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': toDate,
              'fromDate': fromDate,
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result1 = 'PASS'
else:
    result1 = 'FAIL'

print("GET Reports of Payments with report type: CustomTransactionVolume")
parameters = {'reportType': CustomTransactionVolume,
              'toDate': toDate,
              'fromDate': fromDate,
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result2 = 'PASS'
else:
    result2 = 'FAIL'

print("GET Reports of Payments with report type: DuplicatePayments")
parameters = {'reportType': DuplicatePayments,
              'toDate': toDate,
              'fromDate': fromDate
              }
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result3 = 'PASS'
else:
    result3 = 'FAIL'

print("GET Reports of Payments with report type:FlaggedTransactions ")
parameters = {'reportType': FlaggedTransactions,
              'toDate': toDate,
              'fromDate': fromDate}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result4 = 'PASS'
else:
    result4 = 'FAIL'

print("GET Reports of Payments with report type:NonUSDPayments ")
parameters = {'reportType': NonUSDPayments,
              'toDate': toDate,
              'fromDate': fromDate}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result5 = 'PASS'
else:
    result5 = 'FAIL'

print("Verify User NOT able to GET Reports of Payments without Mandatory field ")
parameters = {'reportType': '',
              'toDate': '',
              'fromDate': fromDate,
              'threshold': ''}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode3:
    result6 = 'PASS'
else:
    result6 = 'FAIL'

# If Fromdate is null and ToDate is present ->
print("GET Reports of Payments with: Fromdate is null and ToDate is present")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': toDate,
              'fromDate': '',
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result7 = 'PASS'
else:
    result7 = 'FAIL'

# If Fromdate is present and ToDate is null ->
print("GET Reports of Payments with: Fromdate is present and ToDate is null")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': '',
              'fromDate': fromDate,
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result8 = 'PASS'
else:
    result8 = 'FAIL'

print("GET Reports of Payments with: null threshold")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': '',
              'fromDate': '',
              'threshold': ''}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode3:
    result9 = 'PASS'
else:
    result9 = 'FAIL'

print("GET Reports of Payments with: invalid threshold")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': '',
              'fromDate': '',
              'threshold': 'lkashdlkahsdlk'}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode3:
    result10 = 'PASS'
else:
    result10 = 'FAIL'

print("GET Reports of Payments with: todate is greater than fromdate")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': fromDate,
              'fromDate': toDate,
              'threshold': 10}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode3:
    result11 = 'PASS'
else:
    result11 = 'FAIL'

print("Verify user is not able to GET Reports of Payments with expired token")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': toDate,
              'fromDate': fromDate,
              'threshold': amount}
response = requests.post(url + transactions, headers=expired_header, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode401:
    result12 = 'PASS'
else:
    result12 = 'FAIL'


print("Verify user is not able to GET Reports of Payments without permission")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': toDate,
              'fromDate': fromDate,
              'threshold': amount}
response = requests.post(url + transactions, headers=NoPermission_header, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode403:
    result13 = 'PASS'
else:
    result13 = 'FAIL'

print("GET Reports of Payments with report type: SingleTransactionReportType: " + result1)
print("GET Reports of Payments with report type: CustomTransactionVolume: " + result2)
print("GET Reports of Payments with report type: DuplicatePayments: " + result3)
print("GET Reports of Payments with report type:FlaggedTransactions: " + result4)
print("GET Reports of Payments with report type:NonUSDPayments: " + result5)
print("Verify User NOT able to GET Reports of Payments without Mandatory field : " + result6)
print("GET Reports of Payments with report type: Fromdate is null and ToDate is present: " + result7)
print("GET Reports of Payments with report type: Fromdate is present and ToDate is present: " + result8)
print("GET Reports of Payments with report type: threshold is null: " + result9)
print("GET Reports of Payments with report type: threshold is invalid: " + result10)
print("GET Reports of Payments with report type: todate is greater than fromdate: " + result11)
print("Verify user is not able to GET Reports of Payments with expired token: " + result12)
print("Verify user is not able to GET Reports of Payments without permission: " + result13)