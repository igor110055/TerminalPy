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
from Visualize_SMA import visualize_SMA
SMA5_to_Visualize = visualize_SMA(PriceData, 5)

#Import Strategies
sys.path.insert(3,'/home/hackerboi/Dokumente/python/TerminalPy/Strategies')
from MACrossings import SMAtoSMACompare
SMA5vs10 = SMAtoSMACompare(5,10, Indicator.SMA, PriceData)


#Import Simulator
sys.path.insert(4,'/home/hackerboi/Dokumente/python/TerminalPy/Simulator')
from Runtime import Simulator
Simulation = Simulator(SMA5vs10)
print(Simulation)

#Import Api-Server
sys.path.insert(5,'/home/hackerboi/Dokumente/python/TerminalPy/Server')
from Api import Server
Server(CandleSticks, SMA5_to_Visualize, Simulation)

