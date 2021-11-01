import requests
config = {
    'Symbol': 'BTCUSDT',
    'Interval': {},
    'limit': 1000
}

response = requests.get('https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=200')

json = response.json()

formated = []

for element in json:
    open = round(float(element[1]), 3)
    high = round(float(element[2]), 3)
    low = round(float(element[3]), 3)
    close = round(float(element[4]), 3)
    formated.append([element[0], open, high, low, close])

 
