import requests
import json
import urllib3

urllib3.disable_warnings()

base_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/native/ip/route/ip-route-interface-forwarding-list"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}

response = requests.get(base_url, headers=headers, auth=("developer","C1sco12345"), verify=False).json()
print(json.dumps(response, indent=2))
