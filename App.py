import sys

#Config
#AssetPair, Timeframe for iteration

#Import Candledata
sys.path.insert(1,'/home/hackerboi/Dokumente/python/TerminalPy/PriceData')
import OHLC_data_CCXT
CandleSticks = OHLC_data_CCXT.ohlc

#Import Formated Price Data
from AverageWDate import AveragePrice
PriceData = AveragePrice(CandleSticks)

#Import Indicators (TA-Lib) (For Frontend Visulisation Only)
sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
import Visualize_Indicators
sma5 = Indicator.SMA(PriceData, 5)
sma10 = Indicator.SMA(PriceData, 5)

SMA5_to_Visualize = Visualize_Indicators.visualize_SMA(PriceData, 5) 
RSI_to_Visualize = Visualize_Indicators.visualize_RSI(PriceData, 14)

#Import Strategies
sys.path.insert(3,'/home/hackerboi/Dokumente/python/TerminalPy/Strategies')
from MACrossings import SMAtoSMACompare
SMA5vs10 = SMAtoSMACompare()


#Import Simulator
sys.path.insert(4,'/home/hackerboi/Dokumente/python/TerminalPy/Simulator')
from Runtime import Simulator
Simulation = Simulator(SMA5vs10)

#Import Api-Server
sys.path.insert(5,'/home/hackerboi/Dokumente/python/TerminalPy/Server')
from Api import Server
Server(CandleSticks, [SMA5_to_Visualize, RSI_to_Visualize], Simulation)

