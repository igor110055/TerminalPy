import requests
def PriceDataFetch(Symbol):
    params = {
    'access_key': 'ba7ca8e055c2c866659a548df9fdb01a'
    }
    Url = 'http://api.marketstack.com/v1/eod?access_key=ba7ca8e055c2c866659a548df9fdb01a&symbols='+Symbol
    print(Url)
    # response = requests.get('http://api.marketstack.com/v1/eod?access_key=ba7ca8e055c2c866659a548df9fdb01a&symbols=TEVA.XTAE' ,params)
    response = requests.get(Url)
    json = response.json()
    formated = []

    for element in json['data']:
        open = round(float(element['open']), 3)
        high = round(float(element['high']), 3)
        low = round(float(element['low']), 3)
        close = round(float(element['close']), 3)
        formated.append([element['date'],open, high, low, close])
        

    return formated
