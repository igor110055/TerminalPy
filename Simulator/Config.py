import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/PriceData')
#Import Data
from OHLC_data_CCXT import ohlc

BTCUSDT = ohlc

PriceData = [20,30,40,30,20,35]

#Set Cash Config
TradeCash = 500