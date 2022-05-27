# Takes the Cash/Asset Ballance from every Position and Calculates the PnL relative to the 
# Position before it
import Simulator.PortfolioValue
import Simulator.LiquidationPrices as knock_out

class Formater:

    def __init__(self, HistoryObjFromRuntime2 , price_data):
        self.history = HistoryObjFromRuntime2
        self.price_data = price_data

    def formate(self, leverage=1):
        
        for index in range (0, len(self.history['Trades'])):
            
            trade_position = self.history['Trades'][index]
            # Overwrite leverage optionally
            if leverage != 1:
                trade_position['Leverage'] = leverage

            # Porfolio Totalvalue calculations
            total_portfolio_value_in_cash = Simulator.PortfolioValue.total_portfolio_value(
                trade_position['Current_CashBallance'],
                trade_position['Current_AssetBallance'],
                trade_position['AssetPrice']
            )
            trade_position['TotalPortfolioValue'] = total_portfolio_value_in_cash

        reset_index = [0]

        for index in range(1, len(self.history['Trades'])):

            trade_position = self.history['Trades'][index]
            prev_trade_position = self.history['Trades'][index - 1]

            # PnL Calculations
            asset_price_change_percentage = Simulator.PortfolioValue.calc_price_change(trade_position, prev_trade_position)

            # Calculate the PnL for every previous Position
            if prev_trade_position['Direction'] == 'Long':
                PnL = asset_price_change_percentage * prev_trade_position['Leverage'] 
                trade_position['PnL'] = round(PnL, 2) 
            elif prev_trade_position['Direction'] == 'Short':
                invert_PnL =  (- asset_price_change_percentage) * prev_trade_position['Leverage'] 
                trade_position['PnL'] = round(invert_PnL, 2)


            # Closing positions (as soon as change in direction)
            if trade_position['Direction'] != prev_trade_position['Direction']:
                
                start_closing_index = reset_index.pop(0)
                for pos_closer_index in range(start_closing_index, index):
                    # Close Position
                    self.history['Trades'][pos_closer_index]['Closed'] = trade_position['Open']
                
                reset_index.insert(0, index)

    
    def check_total_long_short_exposure(self):
        for index in range(1, len(self.history['Trades'])):
            # if no change of direction merge Positions
            trade_position = self.history['Trades'][index]
            prev_trade_position = self.history['Trades'][index - 1]

            merge_positions = []

            if trade_position['Direction'] == prev_trade_position['Direction']:
                merge_positions.append([trade_position, prev_trade_position])

            if trade_position['Direction'] != prev_trade_position['Direction'] and len(merge_positions) != 0:
                 
                To = []
                From = []
                Average_AssetPrice = []


                merged_positions = []
                for index in range(0, len(merge_positions)):
                    # Calculate Median AssetPrice (for all Buys/Sells)
                    # Calculate Leverage Factor
                    pos = merge_positions.pop(-1)
                    To.append(pos['To'])
                    From.append(pos['From'])
                    Average_AssetPrice.append(pos['AssetPrice'])

            
            new_position = {
                # from first Position
                'Open': merge_positions[0]['Open'],
                'Direction': prev_trade_position['Direction'],

                'Close': merged_positions[-1]['Closed']
            } 


    def calculate_knockout_price(self):
        for position in self.history['Trades']:
            # calculate liquidation Price
            liquidation_price = knock_out.Test(position)
            # write Liquidation Price back into Position
            position['LiquidationPrice'] = liquidation_price
            position['LiquidationsStatus'] = []
            


    def check_liquidation(self):
        # b00l = len(self.price_data[0]) == len(self.price_data[1])
        prices = dates = self.price_data[1]
        dates = self.price_data[0]

        for position in self.history['Trades']:
            # get index from Open and Close
            opening_index = dates.index(position['Open'])
            if position['Closed'] == 0:
                closing_index = -1
            else:
                closing_index = dates.index(position['Closed'])

            # loop through every positions opening to closing date
            for price_index in range(opening_index,closing_index):
                current_price = prices[price_index]
                liquidation_price = position['LiquidationPrice']

                if position['Direction'] == 'Long':
                    if current_price < liquidation_price:
                        print('REKT at ', current_price, position['AssetPrice'])
                        position['LiquidationsStatus'].append('REKT at ', current_price, position['AssetPrice'])
                elif position['Direction'] == 'Short':
                    if current_price > liquidation_price:
                        print('REKT at ', current_price, position['AssetPrice'], position['ID'])
                        position['LiquidationsStatus'].append('REKT at ', current_price, position['AssetPrice'])
                else:
                    print('No liquidation')
                    position['LiquidationsStatus'].append(False)
                    


# put closing date and closing price for every position and corresponding PnL
# adding pnl from previous position to next is confusing
# add closing condition

