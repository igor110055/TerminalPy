import requests
def PriceDataFetch(Symbol,CandleSize):
    URI = 'https://api.binance.com/api/v3/klines?symbol='+Symbol+'&interval='+CandleSize
    # URI = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=70'
    response = requests.get(URI)
    json = response.json()
    formated = []

    for element in json:
        open = float(element[1])
        high = float(element[2])
        low = float(element[3])
        close = float(element[4])
        formated.append([element[0], open, high, low, close])
    
    return formated