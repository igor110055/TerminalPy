from SimulatorEngine import Engine


class SimulatorOOP:
    def __init__(self, strategy):
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
                executed = self.SimulatorEngine.buy( self.strategy['AssetValue'][index],position['positionSizePercent'])

                if executed == True:
                    # Log all the Metadata
                    self.history['Trades'].append({
                        'Open': self.strategy['Time'][index],
                        'Direction': 'Long',
                        'AssetPrice': self.strategy['AssetValue'][index],
                        'PositionSize': position['positionSizePercent'],
                        'Leverage': position['leverage/factor'],
                        'Current_AssetBallance': self.SimulatorEngine.return_asset()[-1],
                        'Current_CashBallance': self.SimulatorEngine.return_cash()[-1],
                        'Prev_AssetBallance': self.SimulatorEngine.return_asset()[-2],
                        'Prev_CashBallance': self.SimulatorEngine.return_cash()[-2],
                        'From': self.SimulatorEngine.return_prev_position()[-1],
                        'To': self.SimulatorEngine.return_position()[-1],
                        'Closed': 0,
                        'ID': position['id']
                    })

            # Executing the Sell Condition
            elif position['type'] == 'sell':
                
                # execute the Trade by pasing the AssetPrice into the Engine
                executed = self.SimulatorEngine.sell( self.strategy ['AssetValue'][index],position['positionSizePercent'])

                if executed == True:
                    # Log all the Metadata
                    self.history['Trades'].append({
                        'Open': self.strategy ['Time'][index],
                        'Direction':'Short',
                        'AssetPrice': self.strategy ['AssetValue'][index],
                        'PositionSize': position['positionSizePercent'],
                        'Leverage': position['leverage/factor'],
                        'Current_AssetBallance': self.SimulatorEngine.return_asset()[-1],
                        'Current_CashBallance': self.SimulatorEngine.return_cash()[-1],
                        'Prev_AssetBallance': self.SimulatorEngine.return_asset()[-2],
                        'Prev_CashBallance': self.SimulatorEngine.return_cash()[-2],
                        'From': self.SimulatorEngine.return_prev_position()[-1],
                        'To': self.SimulatorEngine.return_position()[-1],
                        'Closed': 0,
                        'ID': position['id']
                    })

    def return_history(self):
        # print('self.history: ',self.history)
        return self.history
