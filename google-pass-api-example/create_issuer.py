import httplib2
import json
from oauth2client.service_account import ServiceAccountCredentials

file_path = './api-google-pay-pass.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    file_path,
    'https://www.googleapis.com/auth/wallet_object.issuer')

http = httplib2.Http()
http = credentials.authorize(http)

issuer_info = {
    "name": "MY_TEST_ISSUER",
    "contactInfo": {
        "email": "example@example.com"
    },
    "smartTapMerchantData": {
        "authenticationKeys": [{
            "id": 1,
            "publicKeyPem": "-----BEGIN PUBLIC KEY-----\n"
                            "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEchyXj869zfmKhRi9xP7f2AK07kEo\n"
                            "4lE7ZlWTN14jh4YBTny+hRGRXcUzevV9zSSPJlPHpqqu5pEwlv1xyFvE1w==\n-----END PUBLIC KEY-----\n"
        }
        ]
    }
}

# Add Issuer
url = 'https://www.googleapis.com/walletobjects/v1/issuer/'
resp, content = http.request(url, 'POST', headers={'Content-Type': 'application/json; charset=UTF-8'}, body=json.dumps(issuer_info))
print "resp : %s - %s\n" % (resp, content)

if resp["status"] == "200":
    jsonResp = json.loads(content)
    issuerId = jsonResp["issuerId"]
    collectorId = jsonResp["smartTapMerchantData"]["smartTapMerchantId"]

print 'collector id: %s' % collectorId
