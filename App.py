# import find_parent
#Config
#AssetPair, Timeframe for iteration

#Import Candledata
# import PriceData.OHLC_data_CCXT
# CandleSticks = OHLC_data_CCXT.ohlc
import PriceData.PriceDataAsJson as PriceDataAsJson
CandleSticks = PriceDataAsJson.PriceDataFetch()

#Import Formated Price Data
from PriceData.AverageWDate import AveragePrice
PriceData = AveragePrice(CandleSticks)

#Import Indicators (TA-Lib) (For Frontend Visulisation Only)
import Indicators.Indicator as Indicator
import Indicators.Visualize_Indicators as Visualize_Indicators
SMA5 = Indicator.SMA(PriceData, 5)
SMA10 = Indicator.SMA(PriceData, 10)

SMA5_to_Visualize = Visualize_Indicators.visualize_SMA(PriceData, 5) 
SMA10_to_Visualize = Visualize_Indicators.visualize_SMA(PriceData, 10) 
RSI_to_Visualize = Visualize_Indicators.visualize_RSI(PriceData, 14)

#Import Strategies

from Strategies.MACrossings import SMAtoSMACompare
SMA5vs10 = SMAtoSMACompare(SMA10 , SMA5)

#Import Simulator

# from Simulator.Runtime import Simulator
# Simulation = Simulator(SMA5vs10)
# from Simulator.RuntimeOutputFormater import Formater
# FormatetTest = Formater(Simulation)

from Simulator.Runtime2 import Simulator2
Simulation2 = Simulator2(SMA5vs10)
from Simulator.RuntimeOutputFormater import Formater2
Formater2Test = Formater2(Simulation2)


#Import Api-Server
# from Server.Api import Server
# Server(CandleSticks, [SMA5_to_Visualize, RSI_to_Visualize], Simulation2)
