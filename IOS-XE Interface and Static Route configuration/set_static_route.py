import requests
import json
import urllib3

urllib3.disable_warnings()

def set_static_route():
    base_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/native"
    static_route_url = base_url + "/ip/route/ip-route-interface-forwarding-list"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-type": "application/yang-data+json",
    }
    config = {
        "Cisco-IOS-XE-native:ip-route-interface-forwarding-list": [
                {
                    "prefix": "10.100.100.0", 
                    "mask": "255.255.255.0", 
                    "fwd-list": [{"fwd":  "17.17.17.17", "name": "restconf-test-route"}]
                }
            ]
        }

    response = requests.patch(static_route_url, headers=headers, data=json.dumps(config), auth=("developer","C1sco12345"), verify=False)
    response_code = response.status_code

    if response_code == 204:
        print("Successfully added/updated static route to desired state.")
    else:
        print(f'Unsuccessfull. The router returned response code {response_code}.')

if __name__ == "__main__":
    set_static_route()
