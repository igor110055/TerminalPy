import Simulator.SimulatorEngine as SimulatorEngine
    
def Simulator2(Strategy):
    # Object thats going to be returned
    History = {
        'AssetPrice': Strategy['AssetValue'],
        'Time': Strategy['Time'],
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
                    
        # Executing the Sell Condition
        elif Strategy['MAonTop'][index] == Strategy['MAMax']['Range']:
            price = Strategy['AssetValue'][index]
            SimulatorEngine.sell(price)
    
    return(History)


