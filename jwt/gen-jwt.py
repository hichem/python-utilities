import jwt
import time

privateKey = """-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC8kGa1pSjbSYZVebtTRBLxBz5H4i2p/llLCrEeQhta5kaQu/Rn
vuER4W8oDH3+3iuIYW4VQAzyqFpwuzjkDI+17t5t0tyazyZ8JXw+KgXTxldMPEL9
5+qVhgXvwtihXC1c5oGbRlEDvDF6Sa53rcFVsYJ4ehde/zUxo6UvS7UrBQIDAQAB
AoGAb/MXV46XxCFRxNuB8LyAtmLDgi/xRnTAlMHjSACddwkyKem8//8eZtw9fzxz
bWZ/1/doQOuHBGYZU8aDzzj59FZ78dyzNFoF91hbvZKkg+6wGyd/LrGVEB+Xre0J
Nil0GReM2AHDNZUYRv+HYJPIOrB0CRczLQsgFJ8K6aAD6F0CQQDzbpjYdx10qgK1
cP59UHiHjPZYC0loEsk7s+hUmT3QHerAQJMZWC11Qrn2N+ybwwNblDKv+s5qgMQ5
5tNoQ9IfAkEAxkyffU6ythpg/H0Ixe1I2rd0GbF05biIzO/i77Det3n4YsJVlDck
ZkcvY3SK2iRIL4c9yY6hlIhs+K9wXTtGWwJBAO9Dskl48mO7woPR9uD22jDpNSwe
k90OMepTjzSvlhjbfuPN1IdhqvSJTDychRwn1kIJ7LQZgQ8fVz9OCFZ/6qMCQGOb
qaGwHmUK6xzpUbbacnYrIM6nLSkXgOAwv7XXCojvY614ILTK3iXiLBOxPu5Eu13k
eUz9sHyD6vkgZzjtxXECQAkp4Xerf5TGfQXGXhxIX52yH+N2LtujCdkQZjXAsGdm
B2zNzvrlgRmgBrklMTrMYgm1NPcW+bRLGcwgW2PTvNM=
-----END RSA PRIVATE KEY-----"""

print( "Private Key:");
print( privateKey );

publicKey = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC8kGa1pSjbSYZVebtTRBLxBz5H
4i2p/llLCrEeQhta5kaQu/RnvuER4W8oDH3+3iuIYW4VQAzyqFpwuzjkDI+17t5t
0tyazyZ8JXw+KgXTxldMPEL95+qVhgXvwtihXC1c5oGbRlEDvDF6Sa53rcFVsYJ4
ehde/zUxo6UvS7UrBQIDAQAB
-----END PUBLIC KEY-----"""

print( "Public Key:" );
print( publicKey );

# Set issued at and expiration time
issuedAt = int(time.time())
expiresAt = issuedAt + 3600 * 24    # token valid for 24 hours

content = {
  "jti": "dfb5f6a0d8d54be1b960e5ffc996f7aa",
  "sub": "71bde130-7738-47b8-8c7d-ad98fbebce4a",
  "scope": [
    "9167ac18-6679-4e44-bbd7-540660c805e6.read:*/*",
    "9167ac18-6679-4e44-bbd7-540660c805e6.write:*/*",
    "9167ac18-6679-4e44-bbd7-540660c805e6.tag:administrator",
    "9167ac18-6679-4e44-bbd7-540660c805e6.configure:*/*"
  ],
  "client_id": "rabbit_client",
  "cid": "rabbit_client",
  "azp": "rabbit_client",
  "grant_type": "password",
  "user_id": "71bde130-7738-47b8-8c7d-ad98fbebce4a",
  "origin": "uaa",
  "user_name": "rabbit_admin",
  "email": "rabbit_admin@example.com",
  "auth_time": issuedAt,
  "rev_sig": "d5cf8503",
  "iat": issuedAt,
  "exp": expiresAt,
  "iss": "http://localhost:8080/uaa/oauth/token",
  "zid": "uaa",
  "aud": [
    "9167ac18-6679-4e44-bbd7-540660c805e6",
    "rabbit_client"
  ]
}

encodedJwt = jwt.encode(content, privateKey, algorithm='RS256', headers={'kid': 'SsZsBNhZcF3Q9S4trpQBTByNRRI'})

print("JWT Token:")
print(encodedJwt.decode('utf8'))

try:
    decodedJwt = jwt.decode(encodedJwt.decode('utf8'), publicKey, audience=['9167ac18-6679-4e44-bbd7-540660c805e6', 'rabbit_client'], algorithms = ['RS256'])

    print("Decoded JWT Token:")
    print(decodedJwt)
    
except jwt.ExpiredSignatureError:
    print ("Validation Error: JWT Expired")
except jwt.exceptions.InvalidAudienceError:
    print ("Validation Error: Invalid Audience")

