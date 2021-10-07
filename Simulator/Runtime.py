import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Strategies')

#import modules
from PriceDiffenrence import PriceDifferencePercentage
import SimulatorEngine

#import Strategy
from MACrossings import SMAtoSMACompare
#Initialize Strategy
SMA5to10 = SMAtoSMACompare(5,10)

#Config
PriceDifference = PriceDifferencePercentage(SMA5to10['AssetValue'])


for element in PriceDifference:
    #Load Strategy in here and give every output signal a buy or a sell
    if SMA5to10['MAonTop'] == 5:
        SimulatorEngine.sell(element)
    else:
        SimulatorEngine.buy(element)

#Adding the TradeCash key/value Pair 
SMA5to10['TradeCash'] = SimulatorEngine.TradeCash
print(SMA5to10)