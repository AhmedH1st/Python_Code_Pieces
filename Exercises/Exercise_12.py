import requests

Bored_site = 'https://www.boredapi.com/api/activity'

response = requests.get(Bored_site)

print(response.json()['activity'])
