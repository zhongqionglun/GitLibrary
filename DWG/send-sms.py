import requests

url = "http://172.28.1.42/api/send_sms"

payload = "{\"text\":\"#param#\",\"port\":[0,0],\"param\":[{\"number\":\"10086\",\"text_param\":[\"bj\"],\"user_id\":1},{\"number\":\"10086\",\"text_param\":[\"ye\"],\"user_id\":2}]}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"d83cfc98cd4946c73843f05fbde1a07e\", uri=\"/api/send_sms\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"WTzWhcbg\", response=\"2d6f61223ff8ad9e77a961d3483557f5\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'Cache-Control': "no-cache",
    'Postman-Token': "7d2304a9-6b2d-4837-b694-4e47390c9784"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)