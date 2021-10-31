import ccxt

exchange = ccxt.binance()
ohlc = exchange.fetch_ohlcv('BTCUSDT','1d')
#print(ohlc)

# def Candles(AssetPair,CandleSize,Exchange):
#     ohlc = Exchange.fetch_ohlcv(AssetPair,CandleSize)
#     return ohlc

# Candles('BTCUSDT','1w', ccxt.binance())