import ccxt

exchange = ccxt.binance()
ohlc = exchange.fetch_ohlcv('BTCUSDT','1w')
#print(ohlc)