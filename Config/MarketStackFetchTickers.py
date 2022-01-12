import requests

def Tickers(exchange):
    params = {
    'access_key': 'ba7ca8e055c2c866659a548df9fdb01a'
    }
    tickers = []

# tickersRaw = requests.get('http://api.marketstack.com/v1/exchanges/'+exchange['mic']+'/tickers', params)
    tickersRaw = requests.get('http://api.marketstack.com/v1/exchanges/XNAS/tickers', params)
    tickersJson = tickersRaw.json()
    for stock in tickersJson['data']['tickers']:
       tickers.append({
        # 'name': exchange,
        'assetPairs': stock['name'],
        'ticker':stock['symbol']
        }) 