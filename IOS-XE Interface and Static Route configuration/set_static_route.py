import requests
import json
import urllib3

urllib3.disable_warnings()

base_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/native"
static_url = base_url + "/ip/route/ip-route-interface-forwarding-list"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}
config = {
    "Cisco-IOS-XE-native:ip-route-interface-forwarding-list": [
            {
                "prefix": "10.10.10.0", 
                "mask": "255.255.255.0", 
                "fwd-list": [{"fwd":  "10.0.0.1", "name": "test1"}]
            }
        ]
    }

response = requests.patch(static_url, headers=headers, data=json.dumps(config), auth=("developer","C1sco12345"), verify=False)
response_code = response.status_code

if response_code == 204:
    print("Successfully added/updated static route to desired state.")
else:
    print(response_code)
