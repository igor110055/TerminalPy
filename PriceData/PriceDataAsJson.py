import requests
BinanceConfig = {
    'BaseUrl': 'https://api.binance.com/api/v3/klines?',
    'Symbol': {
        'BTCUSDT':'symbol=BTCUSDT',
    },
    'Interval': {
        '1Hour':'interval=1h&',
        '1Day':'&interval=1d'
    }
}
URI = BinanceConfig['BaseUrl']+BinanceConfig['Symbol']['BTCUSDT']+BinanceConfig['Interval']['1Day']
 
def PriceDataFetch():
    response = requests.get(URI)
    json = response.json()
    formated = []

    for element in json:
        open = round(float(element[1]), 3)
        high = round(float(element[2]), 3)
        low = round(float(element[3]), 3)
        close = round(float(element[4]), 3)
        formated.append([element[0], open, high, low, close])
    
    return formated