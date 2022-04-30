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
        for index in range(len(self.strategy['Action'])):
            
            position = self.strategy['Action'][index]
            # Executing the Buy Condition
            
            if position['type'] == 'buy':
            
                # execute the Trade by pasing the AssetPrice into the Engine
                self.SimulatorEngine.buy( self.strategy['AssetValue'][index],position['positionSize'])

                # Log all the Metadata
                self.history['Trades'].append({
                    'Open': self.strategy['Time'][index],
                    'Direction': 'Long',
                    'AssetPrice': self.strategy['AssetValue'][index],
                    'PositionSize': position['positionSize'],
                    'Leverage': 1 ,
                    'AssetBallance': self.SimulatorEngine.return_asset()[-1],
                    'CashBallance': self.SimulatorEngine.return_cash()[-1],
                    'From': self.SimulatorEngine.return_prev_position()[-1],
                    'To': self.SimulatorEngine.return_position()[-1]
                })

            # Executing the Sell Condition
            elif position['type'] == 'sell':
                
                # execute the Trade by pasing the AssetPrice into the Engine
                self.SimulatorEngine.sell( self.strategy ['AssetValue'][index],position['positionSize'])

                # Log all the Metadata
                self.history['Trades'].append({
                    'Open': self.strategy ['Time'][index],
                    'Direction':'Short',
                    'AssetPrice': self.strategy ['AssetValue'][index],
                    'PositionSize': position['positionSize'],
                    'Leverage': 1 ,
                    'AssetBallance': self.SimulatorEngine.return_asset()[-1],
                    'CashBallance': self.SimulatorEngine.return_cash()[-1],
                    'From': self.SimulatorEngine.return_prev_position()[-1],
                    'To': self.SimulatorEngine.return_position()[-1]
                })

    def return_history(self):
        # print('self.history: ',self.history)
        return self.history
