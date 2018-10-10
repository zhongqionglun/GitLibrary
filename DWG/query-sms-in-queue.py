import requests

url = "http://172.28.1.42/api/query_sms_in_queue"

headers = {
    'Content-Type': "application/json",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"85498d5c680fff2fb3443132b22f2479\", uri=\"/api/query_sms_in_queue\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"l3dEgF2E\", response=\"acdc7f09eb0ad9cecac54b9283f946e2\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'Cache-Control': "no-cache",
    'Postman-Token': "4212f586-6c37-4462-b391-c623d9f785ee"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)