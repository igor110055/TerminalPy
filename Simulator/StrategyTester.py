#import modules
from PriceDiffenrence import PriceDifferencePercentage
from Config import TradeCash
# from SimulatorEngine import buy
# from SimulatorEngine import sell
import SimulatorEngine

#import Strategy
#import MACrossings

#import Data
from Config import PriceData

#Config Modules
PriceDifference = PriceDifferencePercentage(PriceData)

for element in PriceDifference:
    #Load Strategy in here and give every output signal a buy or a sell
    if element > 30:
        SimulatorEngine.sell(element)
    else:
         SimulatorEngine.buy(element)