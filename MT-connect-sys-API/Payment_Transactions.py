import json
import requests

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

# Get Payment Transactions
print("GET Reports of Payments with report type: SingleTransactionReportType")
parameters = {'reportType': SingleTransactionReportType,
              'toDate': "2021-02-23T05:22:34.699Z",
              'fromDate': "2021-02-23T05:22:34.699Z",
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result1 = 'PASS'
else:
    result1 = 'FAIL'


print("GET Reports of Payments with report type: CustomTransactionVolume")
parameters = {'reportType': CustomTransactionVolume,
              'toDate': "2021-02-23T05:22:34.699Z",
              'fromDate': "2021-02-23T05:22:34.699Z",
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result2 = 'PASS'
else:
    result2 = 'FAIL'


print("GET Reports of Payments with report type: DuplicatePayments")
parameters = {'reportType': DuplicatePayments,
              'toDate': "2021-02-23T05:22:34.699Z",
              'fromDate': "2021-02-23T05:22:34.699Z",
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result3 = 'PASS'
else:
    result3 = 'FAIL'


print("GET Reports of Payments with report type:FlaggedTransactions ")
parameters = {'reportType': FlaggedTransactions,
              'toDate': "2021-02-23T05:22:34.699Z",
              'fromDate': "2021-02-23T05:22:34.699Z",
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result4 = 'PASS'
else:
    result4 = 'FAIL'


print("GET Reports of Payments with report type:NonUSDPayments ")
parameters = {'reportType': NonUSDPayments,
              'toDate': "2021-02-23T05:22:34.699Z",
              'fromDate': "2021-02-23T05:22:34.699Z",
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result5 = 'PASS'
else:
    result5 = 'FAIL'

print("Verify User NOT able to GET Reports of Payments without Mandatory field ")
parameters = {'reportType': '',
              'toDate': "2021-02-23T05:22:34.699Z",
              'fromDate': "2021-02-23T05:22:34.699Z",
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result6 = 'PASS'
else:
    result6 = 'FAIL'


#If Fromdate is null and ToDate is present ->
print("GET Reports of Payments with report type: Fromdate is null and ToDate is present")
parameters = {'reportType': NonUSDPayments,
              'toDate': "2021-02-23T05:22:34.699Z",
              'fromDate': null,
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result7 = 'PASS'
else:
    result7 = 'FAIL'

#If Fromdate is present and ToDate is null ->
print("GET Reports of Payments with report type: Fromdate is present and ToDate is null")
parameters = {'reportType': NonUSDPayments,
              'toDate': null,
              'fromDate': "2021-02-23T05:22:34.699Z",
              'threshold': amount}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters) ,verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result8 = 'PASS'
else:
    result8 = 'FAIL'

print("GET Reports of Payments with report type: amount is null")
parameters = {'reportType': NonUSDPayments,
              'toDate': null,
              'fromDate': null,
              'threshold': null}
response = requests.post(url + transactions, headers=headers, data=json.dumps(parameters), verify=True)
print('Status code: {}'.format(response.status_code))
print('Payload:\n{}'.format(response.text))
if response.status_code == ExpectedCode1:
    result9 = 'PASS'
else:
    result9 = 'FAIL'



print("GET Reports of Payments with report type: SingleTransactionReportType: " + result1)
print("GET Reports of Payments with report type: CustomTransactionVolume: " + result2)
print("GET Reports of Payments with report type: DuplicatePayments: " + result3)
print("GET Reports of Payments with report type:FlaggedTransactions: " + result4)
print("GET Reports of Payments with report type:NonUSDPayments: " + result5)
print("Verify User NOT able to GET Reports of Payments without Mandatory field : " + result6)
print("GET Reports of Payments with report type: Fromdate is null and ToDate is present: " + result7)
print("GET Reports of Payments with report type: Fromdate is present and ToDate is present: " + result8)
print("GET Reports of Payments with report type: amount is null: " + result9)
