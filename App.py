#Config
from Config.Config import PriceData

#Import Indicators (TA-Lib)
import Indicators.Indicator as Indicator
# Declaring 2 Indicators with our Bitcoin PriceData from Config
SMA5 = Indicator.SMA(PriceData, 5)
SMA10 = Indicator.SMA(PriceData, 10)

#Import Strategies
from Strategies.MACrossings import SMAtoSMACompare
# This is a module which compares 2 Moving Averages to each other
# with this output the Simulator module will be able to detect 
# when the Moving Average lines cross each other
SMA5vs10 = SMAtoSMACompare(SMA10 , SMA5)

#Import Simulator
from Simulator.Runtime import Simulator
Simulation = Simulator(SMA5vs10)
# The Output from the Simulater Module needs to be analyzed to 
# tell us if we would have gained or losst money executing that Strategy
from Simulator.RuntimeOutputFormater import Formater
FormatedSimulation = Formater(Simulation)

print(FormatedSimulation)