import requests
import json
import urllib3

urllib3.disable_warnings()

base_url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/native"
gig3 = "/interface/GigabitEthernet=3/"
headers = {
    "Accept": "application/yang-data+json",
    "Content-type": "application/yang-data+json",
}

response = requests.get(base_url+gig3, headers=headers, auth=("developer","C1sco12345"), verify=False).json()
print(json.dumps(response, indent=2))
