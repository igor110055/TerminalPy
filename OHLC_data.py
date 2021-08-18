import ccxt

exchange = ccxt.binance()
ohlc = exchange.fetch_ohlcv('BTCUSDT','1d')
# print(ohlc)