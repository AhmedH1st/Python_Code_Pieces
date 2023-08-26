# Script to get your geo information

import requests

IP_URL = 'https://ipinfo.io/'

response = requests.get(IP_URL)
response_json = response.json()

print(
    f"City:     {response_json['city']}\nRegion:   {response_json['region']}\nCountry:  {response_json['country']}\nLocation  {response_json['loc']}")
