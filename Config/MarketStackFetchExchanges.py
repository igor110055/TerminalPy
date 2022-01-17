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
      })

  MarketStack = {
    'Exchanges': exchanges
    }
  return MarketStack
