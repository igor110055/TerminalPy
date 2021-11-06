import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Strategies')

#import modules
from PriceDiffenrence import PriceDiffPercent
import SimulatorEngine
    
def Simulator(Strategy):
    # Object thats going to be returned
    History = {
        'AssetPrice': Strategy['AssetValue'],
        'Cash': SimulatorEngine.Cash,
        'AssetAmount': SimulatorEngine.Asset,
        'Trades': []
    }

    # Looping through the signals
    for index in range(len(Strategy['MAonTop'])):
        # Executing the Buy Condition
        if Strategy['MAonTop'][index] == Strategy['MAMin']['Range']:
            price = Strategy['AssetValue'][index]
            SimulatorEngine.buy(price)
            
            pnl = PriceDiffPercent(SimulatorEngine.Asset)
            value = SimulatorEngine.Asset[-1]*price
            historyObj = {
                'Time': Strategy['Time'][index],
                'Direction': 'Long',
                'Collateral': {
                    'Type': 'Asset',
                    'Amount': round(SimulatorEngine.Asset[-1], 8),
                    'WorthInCash': round(value),
                    'PnL': round(pnl[-1], 2)
                }
            }

        # Executing the Sell Condition
        elif Strategy['MAonTop'][index] == Strategy['MAMax']['Range']:
            price = Strategy['AssetValue'][index]
            SimulatorEngine.sell(price)
            pnl = PriceDiffPercent(SimulatorEngine.Cash)
            historyObj = {
                'Time': Strategy['Time'][index],
                'Direction': 'Short',
                'Collateral': {
                    'Type': 'Cash',
                    'Amount': round(SimulatorEngine.Cash[-1]),
                    'PnL': round(pnl[-1], 2)
                }
            }

        History['Trades'].append(historyObj)
    
    return(History)


