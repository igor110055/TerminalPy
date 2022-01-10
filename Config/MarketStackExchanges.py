import requests

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

tickers = []
for element in exchanges:
  tickersRaw = requests.get('http://api.marketstack.com/v1/exchanges/'+element['mic']+'/tickers', params)
  tickersJson = tickersRaw.json()
  for stock in tickersJson['data']['tickers']:
    element['stocks'].append({
      'name':stock['name'],
      'ticker':stock['symbol']
    })

lol = 0
