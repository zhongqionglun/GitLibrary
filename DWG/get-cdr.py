import requests

url = "http://172.28.1.42/api/get_cdr"

payload = "{}"
headers = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"f4567f5f1c6f8b87f66210f9e60ff999\", uri=\"/api/query_sms_deliver_status\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"fwiIEdgl\", response=\"bdd9629750a528c0c94bbf9393a2a72a\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'Postman-Token': "37568cb5-a52e-47c7-abd7-98d5ce4820c4"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)