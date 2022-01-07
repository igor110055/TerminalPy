import Simulator.SimulatorEngine as SimulatorEngine
    
def Simulator(Strategy):
    
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
           
            # execute the Trade by pasing the AssetPrice into the Engine
            SimulatorEngine.buy( Strategy['AssetValue'][index] )

            # Log all the Metadata
            History['Trades'].append({
                'Open': Strategy['Time'][index],
                'Direction': 'Long',
                'AssetPrice': Strategy['AssetValue'][index],
                'From': SimulatorEngine.Cash[-1],
                'To': SimulatorEngine.Asset[-1]
            })

        # Executing the Sell Condition
        elif Strategy['MAonTop'][index] == Strategy['MAMax']['Range']:
            
            # execute the Trade by pasing the AssetPrice into the Engine
            SimulatorEngine.sell( Strategy['AssetValue'][index] )

            # Log all the Metadata
            History['Trades'].append({
                'Open': Strategy['Time'][index],
                'Direction':'Short',
                'AssetPrice': Strategy['AssetValue'][index],
                'From': SimulatorEngine.Asset[-1],
                'To': SimulatorEngine.Cash[-1]
            })

    return(History)