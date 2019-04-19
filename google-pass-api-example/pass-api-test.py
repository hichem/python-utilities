import httplib2
from oauth2client.service_account import ServiceAccountCredentials
import loyalty
import merchant

file_path = './api-google-pay-pass.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    file_path,
    'https://www.googleapis.com/auth/wallet_object.issuer')

http = httplib2.Http()
http = credentials.authorize(http)

issuerId = '3247171694516091605'

# GET Issuer information
url = 'https://www.googleapis.com/walletobjects/v1/issuer/' + issuerId
resp, content = http.request(url, 'GET')
print "resp : %s - %s\n" % (resp, content)

# GET LIST OBJECT
url = 'https://www.googleapis.com/walletobjects/v1/loyaltyClass?issuerId=' + issuerId
resp, content = http.request(url, 'GET')
print "resp : %s - %s\n" % (resp, content)

# Create loyalty class
testMerchant = merchant.Merchant('1234', 'test_smb_merchant')
loyalty_class_id = 'loyalty_' + testMerchant.merchantId + '#1'
new_loyalty_class = loyalty.generate_loyalty_class(issuerId, loyalty_class_id)
testMerchant.add_loyalty_class(new_loyalty_class)
url = 'https://www.googleapis.com/walletobjects/v1/loyaltyClass?issuerId=' + issuerId
resp, content = http.request(url, 'POST')
print "resp : %s - %s\n" % (resp, content)
