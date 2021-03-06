# Credentials/Input to get the token
from datetime import datetime
from random import randint

#
# TOKEN_URL = 'https://identity.qa-regalpay.io/connect/token'
# USERNAME = 'chethan@regal-us.com'
# PASSWORD = 'Chethan@1995'
# ACR_VALUES
token_url = 'https://identity.qa-regalpay.io/connect/token'
Username = 'ruchita@regal-us.com'
Password = 'Ruchita@1234'
client_id = 'MineralTreePaymentsOpsApp'
client_secret = 'QN9wyWRJPdr2KTYp'
grant_type = 'password'
Scope = 'openid mtc-sys:manage:setup mtc-sys:view:payments rps-sys:manage:company-configuration mtc-sys:manage:payments'

#
random_value = randint(100, 20000000)
random_value1 = randint(11111, 99999)

# Urls
url1 = 'https://api.qa-regalpay.io'
url = url1 + '/mt-connect-sys/'

transactions = '/transactions'
company_address = 'company-address'
card_account = 'card-account'
ach_account = 'ach-account'
check_account = 'check-account'
setup = 'setup'
entity_setups = 'entity-setups'
entities = 'entities'

add_credentials = 'sftp/add-credentials'
remove_credentials = 'sftp/remove-credentials'
test_connections = 'sftp/test-connection'
default_setup = 'default-setup'
next_check_number = 'next-check-number'

last_batch = 'last-batch'
next_batch_number = 'next-batch-number'
next_settlement_transaction_id = 'next-settlement-transaction-id'
sftp = 'sftp'
sftp_shh = 'sftp/ssh'
sftp_shh_public_key = 'sftp/ssh/public-key'
file_location = 'sftp/file-location'
payment_status = 'payment-upload-status'
current_date = 'batches/currentdate'
batch_status = 'batch-status'
batchnumber = '14'
batch_payments = batchnumber + '/payments'
entityid = ''
update_batch = 'entities/' + entityid + '/batch-upload-status'
true = 'true'

entity_setup = '/entity-setup'
Payment_search = '/search-parameter'
Payments ='/payments'
Disbursement_PaymentsFilename = '/disbursement-filename'
Refund_PaymentsFilename = '/refund-filename'
Payments_transactions = '/transactions'
Refund_Payments = '/refund'
Retry_Payments = '/retry'

Paytype_ACH = 'ACH'
Paytype_CARD = 'CARD'
Paytype_CHECK = 'CHECK'


ExpectedCode = 201
ExpectedCode1 = 200

# User Defined Variables
addressLine1 = 'Regal Regus building'
addressLine2 = 'riverbay'
addressLine3 = 'church street'
city = 'provision house'
state = 'lakeview end'
countryCode = 'IN'
zipCode = '12345-8965'
country = 'India one'

nextCheckNumber = '5'
defaultNumberOfDaysForDisbursement = 5
settlementType1 = 'Batch'
settlementType2 = 'Payment'

compNumber = 'BinaryVarsey'
fundingAlias = 'fundingAlias'
defaultCardValidity = '60'
cardType = 'SingleUse'

ReturnToName = 'MarkCaps'
defaultMailingCodeType = 'MailUSPStoPayee'
defaultHandlingCodeType = 'FedexToPayee'
checkFileName = 'checkFileName'

fileName = 'fileName'

daysToWaitForDisbursement = 5
immediateDestination = 'imDesti998'
immediateDestinationName = 'iDeN89856'
immediateOrigin = 'Ior695328'

immediateOriginName = 'ION123456'
companyId = '56companyId'
formatCode = 'CCD'
originatingDFIId = 'ODFID45'

username = 'admin'
password = 'Atlanta2009!'
credentialName = 'credentialName'
checkFileLocation = '/regal-partners/QAtest/CHEK/'
achFileLocation = '/regal-partners/QAtest/ACH/'
cardFileLocation = '/regal-partners/QAtest/CARD/'
authenticationType1 = 'PrivateKey'
authenticationType2 = 'Password'
authenticationType3 = 'PrivateKeyAndPassword'

Invalid = 'invalid'
privateKeyName = 'privateKeyName'
host = 's-cb0b6465fd3448908.server.transfer.us-east-2.amazonaws.com'
port = '22'

paymentStatus = 'UnConfirmed'
defaultPayType = 'ACH'
paymentType = 'Card'
# start_date = datetime. date(2016, 1, 1)
# end_date = datetime. date(2021, 2, 1)

start_date = '2001-10-08T16:25:06.058Z'
end_date = '2021-10-08T16:25:06.058Z'

SingleTransactionReportType = '1'
CustomTransactionVolume = '2'


ExpiredToken = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IkU3QkM5RTdBNzA4M0ZDMEU0NzNFM0EyNDZCMkI2ODQ2NEJCMzVCMEYiLCJ0eXAiOiJhdCtqd3QiLCJ4NXQiOiI1N3llZW5DRF9BNUhQam9rYXl0b1JrdXpXdzgifQ.eyJuYmYiOjE2MTE3NTIxNzgsImV4cCI6MTYxMTc1Mjc3OCwiaXNzIjoiaHR0cHM6Ly9pZGVudGl0eS5kZXYtcmVnYWxwYXkuaW8iLCJhdWQiOiJNaW5lcmFsVHJlZSBQYXltZW50c09wcyBBcGkiLCJjbGllbnRfaWQiOiJNaW5lcmFsVHJlZVBheW1lbnRzT3BzQXBwIiwic3ViIjoiNDNmMDUyYWQtOGNmZS00ZDVmLTUxZDYtMDhkOGIwYzBkZThmIiwiYXV0aF90aW1lIjoxNjExNzUyMTc3LCJpZHAiOiJsb2NhbCIsIlVzZXJUeXBlIjoiU3lzdGVtIiwic2NvcGUiOlsib3BlbmlkIiwibXRjLXN5czptYW5hZ2U6c2V0dXAiXSwiYW1yIjpbInBhc3N3b3JkIl19.C25n9h2Ljo0iARdDsonVab6eJbbjJpcERWeIyBAhAPfugiV2XpygGNV32KeGD7H-RJhfJiKrgH-yRbLZDbuFTRhKSeH4MczIlIBdrqLmN6RGsK-GEBUYnT4Bov0NMg7zFe7zw-cutt9L6wTUDA0xwCdfw9Elolgb0QW-qWBo-oTyKozNqaxtwQrmyrKi57zvuxAYYTV7MhKtLhqFbSO5U_UCyJ8PVY1UBQWx9bReHYd-y_OA5gQ8TkZo72ziaMQdJPBsUVl9cTB2AvJPjIpKGcbkyM6fI3vVF-hhsWua_nGWJgg7dnTC2j2wp0AVHZIZZMVV8nVS2kHA1sWuRp135g'
InvalidUsername = 'cheth095@gmail.com'
InvalidPassword = 'User@1234'
InvalidTenant_ID= '3a70dfb8-c21e-4831-3b58-08d8b13da1e5'


amount = '100'
DuplicatePayments = 'DuplicatePayments'
FlaggedTransactions = 'FlaggedTransactions'
NonUSDPayments = 'NonUSDPayments'
null = 'null'