from Simulator.PriceDiffenrence import PriceDiffPercent
import Simulator.SimulatorEngine as SimulatorEngine
    
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
                'Direction': 'Long',
                'Open': {
                    'Time': Strategy['Time'][index],
                    'Collateral': 'First Position'
                },
                'Close': {
                    'Time': 'Position is still Open',
                    'Collateral': {
                        'Type': 'Asset',
                        'Amount': round(SimulatorEngine.Asset[-1], 8),
                        'WorthInCash': round(value)
                    }
                },
                
            }

        # Executing the Sell Condition
        elif Strategy['MAonTop'][index] == Strategy['MAMax']['Range']:
            price = Strategy['AssetValue'][index]
            SimulatorEngine.sell(price)
            pnl = PriceDiffPercent(SimulatorEngine.Cash)
            historyObj = {
                'Direction': 'Short',
                'Open': {
                    'Time': Strategy['Time'][index],
                    'Collateral': 'First Position'
                },
                'Close': {
                    'Time': 'Position is still Open',
                    'Collateral': {
                        'Type': 'Cash',
                        'Amount': round(SimulatorEngine.Cash[-1]),
                        'PnL': round(pnl[-1], 2)
                    }
                },
            }

        History['Trades'].append(historyObj)
    
    return(History)


