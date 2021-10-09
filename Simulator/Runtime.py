import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Strategies')

#import modules
from PriceDiffenrence import PriceDifferencePercentage
import SimulatorEngine

def Simulator(Strategy):

    PriceDifference = PriceDifferencePercentage(Strategy['AssetValue'])

    for element in PriceDifference:
        #Load Strategy in here and give every output signal a buy or a sell
        if Strategy['MAonTop'] == 5:
            SimulatorEngine.buy(element)
        else:
            SimulatorEngine.sell(element)

    #Adding the TradeCash key/value Pair 
    Strategy['TradeCash'] = SimulatorEngine.TradeCash
    return(Strategy)