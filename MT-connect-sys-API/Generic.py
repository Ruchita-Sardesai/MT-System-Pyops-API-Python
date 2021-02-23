# Credentials/Input to get the token
from random import randint

token_url = 'https://identity.dev-regalpay.io/connect/token'
Username = 'ruchita@regal-us.com'
Password = 'Ruchita@12345'
client_id = 'MineralTreePaymentsOpsApp'
client_secret = 'QN9wyWRJPdr2KTYp'
grant_type = 'password'
Scope = 'openid mtc-sys:manage:setup'

#
random_value = randint(100, 20000000)
random_value1 = randint(11111, 99999)
# Urls
url = 'https://api.dev-regalpay.io/mt-connect-sys/'

transactions = '/transactions'
company_address = 'company-address'
card_account = 'card-account'
ach_account = 'ach-account'
check_account = 'check-account'
setup = 'setup'
add_credentials = 'add-credentials'
remove_credentials = 'remove-credentials'
test_connections = 'test-connection'
default_setup = 'default-setup'
next_check_number = 'next-check-number'
entity_setup = 'entity-setup'
last_batch = 'last-batch'
Tenant_ID = '3a70dfb8-c21e-4831-2b58-08d8b13da1e5'

# User Defined Variables
addressLine1 = 'Regal Regus building'
addressLine2 = 'riverbay'
addressLine3 = 'church street'
city = 'provision house'
state = 'lakeview end'
countryCode = 'IN'
zipCode = '12345-8965'
country = 'India one'

nextCheckNumber = random_value
defaultNumberOfDaysForDisbursement = 5
settlementType1 = 'Batch'
settlementType2 = 'Payment'

fundingAlias = 'fundingAlias'
defaultCardValidity = '60'
cardType = 'SingleUse'

defaultMailingCodeType = 'MailUSPStoPayee'
defaultHandlingCodeType = 'FedexToPayee'
checkFileName = 'checkFileName'

fileName = 'fileName'
immediateDestination = 'immediateDestination'
immediateDestinationName = 'immediateDestinationName'
immediateOrigin = '695328'
immediateOriginName = '123456'
companyId = 'companyId'
formatCode = 'PPD'

daysToWaitForDisbursement = 5
defaultPayType = 'Check'

username = 'admin'
password = 'Atlanta2009!'
credentialName = 'credentialName'
checkFileLocation = 'checkFileLocation'
achFileLocation = 'achFileLocation'
cardFileLocation = 'cardFileLocation'

SingleTransactionReportType = '1'
CustomTransactionVolume = '2'
DuplicatePayments = '3'
FlaggedTransactions = '4'
NonUSDPayments = '5'

amount = '100.00'
null = 'null'

ExpectedCode = 201
ExpectedCode1 = 200

#
ExpiredToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkU3QkM5RTdBNzA4M0ZDMEU0NzNFM0EyNDZCMkI2ODQ2NEJCMzVCMEYiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiI1N3llZW5DRF9BNUhQam9rYXl0b1JrdXpXdzgifQ.eyJuYmYiOjE2MTE3NTIxNzgsImV4cCI6MTYxMTc1Mjc3OCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5kZXYtcmVnYWxwYXkuaW8iLCJhdWQiOiJNaW5lcmFsVHJlZSBQYXltZW50c09wcyBBcGkiLCJjbGllbnRfaWQiOiJNaW5lcmFsVHJlZVBheW1lbnRzT3BzQXBwIiwic3ViIjoiNDNmMDUyYWQtOGNmZS00ZDVmLTUxZDYtMDhkOGIwYzBkZThmIiwiYXV0aF90aW1lIjoxNjExNzUyMTc3LCJpZHAiOiJsb2NhbCIsIlVzZXJUeXBlIjoiU3lzdGVtIiwic2NvcGUiOlsib3BlbmlkIiwibXRjLXN5czptYW5hZ2U6c2V0dXAiXSwiYW1yIjpbInBhc3N3b3JkIl19.C25n9h2Ljo0iARdDsonVab6eJbbjJpcERWeIyBAhAPfugiV2XpygGNV32KeGD7H-RJhfJiKrgH-yRbLZDbuFTRhKSeH4MczIlIBdrqLmN6RGsK-GEBUYnT4Bov0NMg7zFe7zw-cutt9L6wTUDA0xwCdfw9Elolgb0QW-qWBo-oTyKozNqaxtwQrmyrKi57zvuxAYYTV7MhKtLhqFbSO5U_UCyJ8PVY1UBQWx9bReHYd-y_OA5gQ8TkZo72ziaMQdJPBsUVl9cTB2AvJPjIpKGcbkyM6fI3vVF-hhsWua_nGWJgg7dnTC2j2wp0AVHZIZZMVV8nVS2kHA1sWuRp135g'
InvalidUsername = 'cheth095@gmail.com'
InvalidPassword = 'User@1234'
InvalidTenant_ID= '3a70dfb8-c21e-4831-3b58-08d8b13da1e5'
