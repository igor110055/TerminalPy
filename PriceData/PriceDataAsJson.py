import requests

response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d')

print(response.json())