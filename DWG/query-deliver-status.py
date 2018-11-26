import requests


def query_diliver_status(urladdr, jsondata, reqheaders):
    response = requests.request("POST", urladdr, jsondata, reqheaders)
    return response


if __name__ == "__main__":
    url = "http://172.28.1.42/api/query_sms_deliver_status"
    payload = "{port\":[0,0],\"number\":\"10086\",\"user_id\":1}"
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Digest username=\"admin\", realm=\"Web Server\", nonce=\"f4567f5f1c6f8b87f66210f9e60ff999\", uri=\"/api/query_sms_deliver_status\", algorithm=\"MD5\", qop=auth, nc=00000001, cnonce=\"fwiIEdgl\", response=\"bdd9629750a528c0c94bbf9393a2a72a\", opaque=\"5ccc069c403ebaf9f0171e9517f40e41\"",
        'Cache-Control': "no-cache",
        'Postman-Token': "44aafaed-755e-42b1-a4c0-5338d396e7e3"
    }
    resp = query_diliver_status(url, payload, headers)
    if not resp:
        print("The response is empty!")
    else:
        print(resp.text)
