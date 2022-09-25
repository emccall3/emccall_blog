import requests
import json
import urllib3

urllib3.disable_warnings()

base_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/Cisco-IOS-XE-native:native"
url_gig3 = base_url + "/interface/GigabitEthernet=3/ip/address/primary"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}
config = {"primary": {"address": "192.168.77.1", "mask": "255.255.255.252"}}


response = requests.put(url_gig3, headers=headers, data=json.dumps(config), auth=("developer","C1sco12345"), verify=False)
response_code = response.status_code
print(response_code)
