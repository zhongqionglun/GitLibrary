import requests

url = "http://172.28.1.42/api/set_config"

payload = "{ \"sip_trunk\":[{\"index\":31,\"enable\":\"on\",\"domain\":\"172.28.1.46\",\"port\":5060,\"description\":\"benji\",\"check_network_status\":\"on\"}] }"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"2b4c82af05bbbd60d2abff09f2461a63\", uri=\"/api/set_config\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"X7F4hPdi\", response=\"8ab017746bf7e002c50bcbc211b07607\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'cache-control': "no-cache",
    'Postman-Token': "997ab256-49e1-47d0-925b-10b79ae76b13"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)