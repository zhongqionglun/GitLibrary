import requests

url = "http://172.28.1.42/api/query_incoming_sms"

headers = {
    'Content-Type': "application/json",
    'flag': "all",
    'port': "0",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"0ef4291683b2e29974c078f47dc910f7\", uri=\"/api/query_incoming_sms\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"UGO58uRk\", response=\"e8f69d461c98099f11988d05c7d2c73e\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'Cache-Control': "no-cache",
    'Postman-Token': "386e6e56-c7a9-44e7-bf47-a4b93cb82a18"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)