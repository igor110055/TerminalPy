import requests

def MarketStackData():
  params = {
    'access_key': 'ba7ca8e055c2c866659a548df9fdb01a'
  }

  exchanges = []
  
  exchangesRaw = requests.get('http://api.marketstack.com/v1/exchanges', params)
  exchangesJson = exchangesRaw.json()
  for element in exchangesJson['data']:
    exchanges.append({
      'name':element['name'],
      'mic':element['mic'],
      'stocks':[]
      })

  # tickers = []

  for element in exchanges:
    tickersRaw = requests.get('http://api.marketstack.com/v1/exchanges/'+element['mic']+'/tickers', params)
    tickersJson = tickersRaw.json()
    for stock in tickersJson['data']['tickers']:
      element['stocks'].append({
        'name':stock['name'],
        'ticker':stock['symbol']
      })

  MarketStack = {
    'Exchanges': exchanges,
    'CandleSize':{
      'Minute1' : '1min',
      'Minutes5': '5min',
      'Minutes10': '10min',
      'Minutes15' : '15min',
      'Minutes30' : '30min',
      '1Hour': '1hour', 
      '3Hours': '3hour',
      '6Hours' : '6hour',
      '12Hours' : '12hour',
      '1Day': '24hour',
    }
  }
  return MarketStack
