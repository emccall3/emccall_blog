import json
import requests
import urllib3

urllib3.disable_warnings()

def delete_ip():

    base_url = "https://sandbox-iosxe-latest-1.cisco.com"
    headers = {
        "Accept": "application/yang-data+json",
        "Content-type": "application/yang-data+json",
    }
    endpoint = "/restconf/data/native/interface/GigabitEthernet=3/ip/address/primary"
    response = requests.delete(base_url+endpoint, headers=headers, auth=("developer","C1sco12345"), verify=False, timeout=20)
    code = response.status_code
    print(code)

if __name__ == "__main__":
    delete_ip()
