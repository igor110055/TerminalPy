from Simulator.PriceDiffenrence import PriceDiffPercent
import Simulator.SimulatorEngine as SimulatorEngine
    
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

        elif Strategy['MAonTop'][index] == 10:
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


