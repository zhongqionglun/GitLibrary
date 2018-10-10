import requests

url = "http://172.28.1.42/api/query_sms_result"

payload = "{port\":[0,0],\"number\":\"10086\",\"user_id\":1}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"ad86841c71da9a3f88679ee01d2f1ed2\", uri=\"/api/query_sms_result\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"4Efsy2xG\", response=\"0674bea4c2ef6acaadd48d4f5bdf9a3b\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'Cache-Control': "no-cache",
    'Postman-Token': "7390ebd5-13e2-40c4-9ffb-9c0e534f3580"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)