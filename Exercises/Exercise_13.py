# Script to suggest activities for you Once you run

import requests

IP_URL = 'https://api.ipify.org?format=json'

response = requests.get(IP_URL)

print(response.json()['ip']) 
