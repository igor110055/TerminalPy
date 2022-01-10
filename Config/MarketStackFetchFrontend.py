import requests
def PriceDataFetch(Symbol,CandleSize):
    params = {
    'access_key': 'ba7ca8e055c2c866659a548df9fdb01a'
    }
    response = requests.get('http://api.marketstack.com/v1/intraday&symbol='+Symbol+'&interval='+CandleSize ,params)
    json = response.json()
    formated = []

    # for element in json:
    #     open = round(float(element[1]), 3)
    #     high = round(float(element[2]), 3)
    #     low = round(float(element[3]), 3)
    #     close = round(float(element[4]), 3)
    #     formated.append([element[0], open, high, low, close])

    # return formated
