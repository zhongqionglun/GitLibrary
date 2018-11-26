import requests

url = "http://172.28.1.42/api/set_config"

payload = "{\"ip_to_tel_routing\":[{\"index\":1,\"enable\":\"on\",\"description\":\"cs\",\"src_mode\":\"sip_trunk\",\"src_id\":31,\"dst_mode\":\"port\",\"dst_id\":0,\"operation\":\"Forbid\",\"src_prefix\":\"\",\"dst_prefix\":\"\",\"prefix_to_be_added\":\"\",\"suffix_to_be_added\":\"\",\"del_digit\":0,\"reserve_digit\":0}]}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"28a1e391eaa89e1ab7bc45a8efbfd110\", uri=\"/api/set_config\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"lRWyKMkq\", response=\"b98364f80fb6df2bd0c4763fa4bd2471\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
    'cache-control': "no-cache",
    'Postman-Token': "6fcc071e-e980-4050-bdbb-ad4a1f01282a"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)