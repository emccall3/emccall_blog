'''
This script will create or update the IP address of an interface (specifically GigabitEthernet3 as written)
After some initial data is collected, a try/except block will initially try to retreive the IP configuration.
If the retreival is successful, there are two options: 
    1) The configuration of the IP and Mask match what is in our config dictionary and no further action is taken.
    2) The configuration does not match and we replace it with a "patch" operation.
If the retreival is unsuccessfull, then the configuration must not exist. In this case we create the IP address and mask with a "put" operation
'''

import json
import requests
import urllib3
from rich import print as rprint

urllib3.disable_warnings()

def set_ip():
    address = input("Enter IP address: ")
    mask = input("Enter network mask: ")

    base_url = "https://sandbox-iosxe-latest-1.cisco.com"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-type": "application/yang-data+json",
    }
    config = {"Cisco-IOS-XE-native:primary": {"address": address, "mask": mask}}
    endpoint = "/restconf/data/native/interface/GigabitEthernet=3/ip/address/primary"
    
    try:

        response = requests.get(base_url+endpoint, headers=headers, auth=("developer","C1sco12345"), verify=False, timeout=20).json()
        if response == config:
            rprint('[green] No update. [/green] The existing configuration matches the configuration attempted.')
        else:
            response = requests.patch(base_url+endpoint, headers=headers, data=json.dumps(config), auth=("developer","C1sco12345"), verify=False, timeout=20)
            #response_code = response.status_code
            #print(response_code)
            rprint('[green] Updated. [/green] The existing configuration has been updated.')

    except:
        response = requests.put(base_url+endpoint, headers=headers, data=json.dumps(config), auth=("developer","C1sco12345"), verify=False, timeout=20)
        #response_code = response.status_code
        #print(response_code)
        rprint('[green] Created. [/green] The existing configuration has been created.')

if __name__ == "__main__":
    set_ip()
