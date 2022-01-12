#Config
from Config.Config import PriceData

#Import Indicators (TA-Lib)
import Indicators.Indicator as Indicator
SMA5 = Indicator.SMA(PriceData, 5)
SMA10 = Indicator.SMA(PriceData, 10)

#Import Strategies
from Strategies.MACrossings import SMAtoSMACompare
SMA5vs10 = SMAtoSMACompare(SMA10 , SMA5)

#Import Simulator
from Simulator.Runtime import Simulator
Simulation = Simulator(SMA5vs10)
from Simulator.RuntimeOutputFormater import Formater
FormatedSimulation = Formater(Simulation)

print(FormatedSimulation)