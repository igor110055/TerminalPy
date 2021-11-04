import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Strategies')

#import modules
from PriceDiffenrence import PriceDiffPercent
import SimulatorEngine
    
def Simulator(Strategy):
    History = {
        'AssetPrice': Strategy['AssetValue'],
        'Cash': SimulatorEngine.Cash,
        'AssetAmount': SimulatorEngine.Asset,
        'Trades': []
    }

    for index in range(len(Strategy['MAonTop'])):
        if Strategy['MAonTop'][index] == 5:
            price = Strategy['AssetValue'][index]
            SimulatorEngine.buy(price)
            
            pnl = PriceDiffPercent(SimulatorEngine.Asset)
            time = Strategy['Time'][index]
            value = SimulatorEngine.Asset[-1]*price
            historyObj = {
                'Time': time,
                'Direction': 'Long',
                'Collateral': {
                    'Type': 'Asset',
                    'Amount': round(SimulatorEngine.Asset[-1], 8),
                    'WorthInCash': round(value),
                    'PnL': round(pnl[-1], 2)
                }
            }

        elif Strategy['MAonTop'][index] == 10:
            price = Strategy['AssetValue'][index]
            SimulatorEngine.sell(price)
            
            pnl = PriceDiffPercent(SimulatorEngine.Cash)
            time = Strategy['Time'][index]
            historyObj = {
                'Time': time,
                'Direction': 'Short',
                'Collateral': {
                    'Type': 'Cash',
                    'Amount': round(SimulatorEngine.Cash[-1]),
                    'PnL': round(pnl[-1], 2)
                }
            }

        History['Trades'].append(historyObj)
    
    return(History)










# import sys
# sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Strategies')

# #import modules
# from PriceDiffenrence import PriceDifferencePercentage
# import SimulatorEngine

# def Simulator(Strategy):

#     PriceDifference = PriceDifferencePercentage(Strategy['AssetValue'])

#     for element in PriceDifference:
#         #Load Strategy in here and give every output signal a buy or a sell
#         if Strategy['MAonTop'] == 5:
#             SimulatorEngine.buy(element)
#         else:
#             SimulatorEngine.sell(element)

#     #Adding the TradeCash key/value Pair 
#     Strategy['TradeCash'] = SimulatorEngine.TradeCash
#     return(Strategy)