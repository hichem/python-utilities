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

# Set redemption issuer (MY_TEST_ISSUER)
redemptionIssuerId = '3321328218083860406'

# GET Issuer information
url = 'https://www.googleapis.com/walletobjects/v1/issuer/' + redemptionIssuerId
resp, content = http.request(url, 'GET')
print "resp : %s - %s\n" % (resp, content)

# Set Loyalty Class Parameters
merchantId = '567237'
merchantName = "MyTestMerchant"
loyaltyClassName = "MyTestClass"
loyaltyClassDescriptor = {
    'accountIdLabel': 'Member Id',
    'accountNameLabel': 'Member Name',
    'allowMultipleUsersPerObject': True,
    'id': '%s.%s' % (issuerId, loyaltyClassName),
    'issuerName': 'Test Loyalty Service',
    'kind': 'walletobjects#loyaltyClass',
    'locations': [{
        'kind': 'walletobjects#latLongPoint',
        'latitude': 37.424015499999996,
        'longitude': -122.09259560000001
    }, {
        'kind': 'walletobjects#latLongPoint',
        'latitude': 37.424354,
        'longitude': -122.09508869999999
    }, {
        'kind': 'walletobjects#latLongPoint',
        'latitude': 37.7901435,
        'longitude': -122.39026709999997
    }, {
        'kind': 'walletobjects#latLongPoint',
        'latitude': 40.7406578,
        'longitude': -74.00208940000002
    }],
    'textModulesData': [{
        'header': 'Rewards details',
        'body': '\u00B0 \u00ae \u00a9 Welcome to Baconrista rewards.  Enjoy your rewards for being a loyal customer. ' +
                '10 points for every dollar spent.  Redeem your points for free coffee, bacon and more!'
    }],
    'linksModuleData': {
        'uris': [
            {
                'kind': 'walletobjects#uri',
                'uri': 'http://maps.google.com/?q=google',
                'description': 'Nearby Locations'
            }, {
                'kind': 'walletobjects#uri',
                'uri': 'tel:6505555555',
                'description': 'Call Customer Service'
            }]
    },
    'infoModuleData': {
        'hexFontColor': '#F8EDC1',
        'hexBackgroundColor': '#442905'
    },
    'imageModulesData': [
        {
            'mainImage': {
                'kind': 'walletobjects#image',
                'sourceUri': {
                    'kind': 'walletobjects#uri',
                    'uri': 'http://farm4.staticflickr.com/3738/12440799783_3dc3c20606_b.jpg',
                    'description': 'Coffee beans'
                }
            }
        }
    ],
    'messages': [{
        'actionUri': {
            'kind': 'walletobjects#uri',
            'uri': 'http://baconrista.com'
        },
        'header': 'Welcome to Banconrista Rewards!',
        'body': 'Featuring our new bacon donuts.',
        'image': {
            'kind': 'walletobjects#image',
            'sourceUri': {
                'kind': 'walletobjects#uri',
                'uri': 'http://farm8.staticflickr.com/7302/11177240353_115daa5729_o.jpg'
            }
        },
        'kind': 'walletobjects#walletObjectMessage'
    }],
    'programLogo': {
        'kind': 'walletobjects#image',
        'sourceUri': {
            'kind': 'walletobjects#uri',
            'uri': 'https://cdn.example.com/images/logo.png'
        }
    },
    'programName': '%s Rewards' % merchantName,
    'enableSmartTap': 'true',
    'redemptionIssuers': [
        '%s' % redemptionIssuerId
    ],
    'rewardsTier': 'Gold',
    'rewardsTierLabel': 'Tier',
    'reviewStatus': 'underReview'
}

url = 'https://www.googleapis.com/walletobjects/v1/loyaltyClass'
resp, content = http.request(url, 'POST',
                             headers={'Content-Type': 'application/json; charset=UTF-8'},
                             body=json.dumps(loyaltyClassDescriptor))
print "resp : %s - %s\n" % (resp, content)
