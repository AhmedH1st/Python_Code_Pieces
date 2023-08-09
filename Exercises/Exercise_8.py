#Get the current price of Bitcoin
import requests

TICKER_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
crypto = 'bitcoin'
response = requests.get(TICKER_API_URL)
response_json = response.json()
price = float(response_json["bpi"]["USD"]["rate_float"])
print(price)



