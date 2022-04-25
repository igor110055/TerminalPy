from Simulator.SimEngineOOP import Engine


class SimulatorOOP:
    def __init__(self, strategy) -> None:
        """Load Strategy Data"""
        self.strategy = strategy
        self.SimulatorEngine = Engine()
        # Object thats going to be returned
        self.history = {
            'AssetPrice': strategy['AssetValue'],
            'Time': strategy['Time'],
            'Trades': []
        }

    def execute(self):
        for element in self.strategy['Action']:
            self.index = self.strategy['Action'].index(element)
            # Executing the Buy Condition
            if element['type'] == 'buy':
            
                # execute the Trade by pasing the AssetPrice into the Engine
                self.SimulatorEngine.buy( self.strategy['AssetValue'][self.index],element['positionSize'])

                # Log all the Metadata
                self.history['Trades'].append({
                    'Open': self.strategy['Time'][self.index],
                    'Direction': 'Long',
                    'AssetPrice': self.strategy['AssetValue'][self.index],
                    'PositionSize': element['positionSize'],
                    'Leverage': 1 ,
                    'From': self.SimulatorEngine.return_cash()[-1],
                    'To': self.SimulatorEngine.return_asset()[-1]
                })

            # Executing the Sell Condition
            elif element['type'] == 'sell':
                
                # execute the Trade by pasing the AssetPrice into the Engine
                self.SimulatorEngine.sell( self.strategy ['AssetValue'][self.index],element['positionSize'])

                # Log all the Metadata
                self.history['Trades'].append({
                    'Open': self.strategy ['Time'][self.index],
                    'Direction':'Short',
                    'AssetPrice': self.strategy ['AssetValue'][self.index],
                    'PositionSize': element['positionSize'],
                    'Leverage': 1 ,
                    'From': self.SimulatorEngine.return_asset()[-1],
                    'To': self.SimulatorEngine.return_cash()[-1]
                })

    def return_history(self):
        # print('self.history: ',self.history)
        return self.history
