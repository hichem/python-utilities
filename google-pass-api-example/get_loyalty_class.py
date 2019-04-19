import httplib2
from oauth2client.service_account import ServiceAccountCredentials
import json

file_path = './api-google-pay-pass.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    file_path,
    'https://www.googleapis.com/auth/wallet_object.issuer')

http = httplib2.Http()
http = credentials.authorize(http)

# Set Issuer ID
issuerId = '3247171694516091605'


# Set Loyalty Class Parameters
merchantId = '567237'
merchantName = "MyTestMerchant"
loyaltyClassName = "MyTestClass"


url = 'https://www.googleapis.com/walletobjects/v1/loyaltyClass/' + issuerId + "." + loyaltyClassName
resp, content = http.request(url, 'GET')
print "resp : %s - %s\n" % (resp, content)
