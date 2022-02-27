import requests
from datetime import datetime
import copy
def PriceDataFetch(Symbol,CandleSize):
    URI = 'https://api.binance.com/api/v3/klines?symbol='+Symbol+'&interval='+CandleSize
    # +'&limit=70'

    response = requests.get(URI)
    json = response.json()
    formated = []

    for element in json:
        # copy.deepcopy(str
        date = datetime.fromtimestamp(element[0]/1000).isoformat()
        open = float(element[1])
        high = float(element[2])
        low = float(element[3])
        close = float(element[4])
        formated.append([date, open, high, low, close])
    
    return formated