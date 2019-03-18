import requests

url = "http://172.28.1.42/api/send_sms"

payload = "{\"text\":\"#param#\",\"port\":[0,0]," \
          "\"param\":[{\"number\":\"10086\",\"text_param\":[\"ye\"],\"user_id\":1}]}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"54afc52d9050c1be4baa3a5c6fa19f67\", "
                     "uri=\"/api/send_sms\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"WcxI1D42\","
                     " response=\"f2d53f57a1a42676821bdef76806abd1\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'cache-control': "no-cache",
    'Postman-Token': "15399f57-f02a-4098-907c-307ba492a907"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)