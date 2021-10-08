import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Server')

#Config
#AssetPair
#CandleSize

#Import Price Data
sys.path.insert(1, '/home/hackerboi/Dokumente/python/TerminalPy/PriceData')
from AverageWDate import Average

#Import Indicators (TA-Lib) (For Frontend)
sys.path.insert(2, '/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
# SMA = Indicator.SMA

#Import Strategies
sys.path.insert(3, '/home/hackerboi/Dokumente/python/TerminalPy/Strategies')
from MACrossings import SMAtoSMACompare
SMA5vs10 = SMAtoSMACompare(5,10, Indicator.SMA, Average)

#Import Simulator
sys.path.insert(4, '/home/hackerboi/Dokumente/python/TerminalPy/Simulator')
import Runtime
print(Runtime.Simulator(SMA5vs10))

#Import Dependencies
from Api import Server
#Server(ohlc, Indicators, Simulator)

