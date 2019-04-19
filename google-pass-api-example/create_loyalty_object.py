import httplib2
from oauth2client.service_account import ServiceAccountCredentials
import json

file_path = './api-google-pay-pass-.json'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    file_path,
    'https://www.googleapis.com/auth/wallet_object.issuer')

http = httplib2.Http()
http = credentials.authorize(http)

# Set Issuer ID
issuer_id = '3247171694516091605'

# Set redemption issuer (MY_TEST_ISSUER)
redemption_issuer_id = '3321328218083860406'

# Set Loyalty Class Name
class_name = "MyTestClass"

# Set object name
user_id = "1234567890"
account_name = "John Doe"
loyalty_object_name = "%s_loyalty_object" % user_id

# Create loyalty object
loyalty_object = {
  'classId': '%s.%s' % (issuer_id, class_name),
  'id': '%s.%s' % (issuer_id, loyalty_object_name),
  'accountId': '%s' % user_id,
  'accountName': '%s' % account_name,
  'barcode': {
      'alternateText' : '%s' % user_id,
      'type': 'qrCode',
      'value': '%s' % user_id
  },
  'textModulesData': [{
    'header': '%s\'s Loyalty Card' % account_name,
    'body': 'Your Fidelity Rewarded!!!'
  }],
  'linksModuleData': {
    'uris': [
      {
        'kind': 'walletobjects#uri',
        'uri': 'http://www.example.com/vas/user/myaccount?id=%s' % user_id,
        'description': 'URL to customer loyalty account'
      }]
  },
  'infoModuleData': {
    'labelValueRows': [{
        'columns': [{
          'label': 'Next Reward in',
          'value': '2 coffees'
        }, {
          'label': 'Member Since',
          'value': '01/15/2013'
        }]
      },{
        'columns': [{
          'label': 'Local Store',
          'value': 'Mountain View'
        }]
    }],
    'showLastUpdateTime': 'true'
  },
  'loyaltyPoints': {
      'balance': {
          'string': '500'
      },
      'label': 'Points',
      'pointsType': 'points'
  },
  'state': 'active',
  'version': 1
}

url = 'https://www.googleapis.com/walletobjects/v1/loyaltyObject'
resp, content = http.request(url, 'POST',
                             headers={'Content-Type': 'application/json; charset=UTF-8'},
                             body=json.dumps(loyalty_object))
print "resp : %s - %s\n" % (resp, content)


