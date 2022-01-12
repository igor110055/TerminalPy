import requests
def BinanceMetaData():
    response = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    json = response.json()

    Binance = {
        'name':'Binance',
        'assetPairs':[],
        'CandleSize' : {
            'Minute1' : '1m',
            'Minutes3' : '3m',
            'Minutes5': '5m',
            'Minutes15' : '15m',
            'Minutes30' : '30m',
            '1Hour': '1h', 
            '2Hours': '2h',
            '4Hours' : '4h',
            '6Hours' : '6h',
            '8Hours' : '8h',
            '12Hours' : '12h',
            '1Day': '1d',
            '3Days' : '3d',
            '1Week': '1w',
            '1Month': '1M'
        }
    }

    for element in json['symbols']:
        Binance['AssetPairs'].append(element['symbol'])

    Binance['AssetPairs'].sort()
    
    return Binance
