import httplib2
from oauth2client.service_account import ServiceAccountCredentials

file_path = './api-google-pay-pass.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    file_path,
    'https://www.googleapis.com/auth/wallet_object.issuer')

http = httplib2.Http()
http = credentials.authorize(http)

# GET all issuers
url = 'https://www.googleapis.com/walletobjects/v1/issuer/'
resp, content = http.request(url, 'GET')
print "resp : %s - %s\n" % (resp, content)
