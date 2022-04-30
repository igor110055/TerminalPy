# Takes the Cash/Asset Ballance from every Position and Calculates the PnL relative to the 
# Position before it

def Formater(HistoryObjFromRuntime2):
    for index in range(1, len(HistoryObjFromRuntime2['Trades'])):
        element1 = HistoryObjFromRuntime2['Trades'][index - 1]['From']     
        element2 = HistoryObjFromRuntime2['Trades'][index]['To']  
        if element1 == 0:
            continue
        changePercentage = ((element2 / element1) - 1) * 100
        # Adding a PnL key/value pair to each trade
        HistoryObjFromRuntime2['Trades'][index]['PnL'] =  round(changePercentage, 2)      

    return HistoryObjFromRuntime2

import Simulator.PortfolioValue
import Simulator.LiquidationPrices

class FormaterC:
    def __init__(self, HistoryObjFromRuntime2 , price_data):
        self.unformated_history = HistoryObjFromRuntime2
        self.price_data = price_data

    def formate(self, leverage):
        for index in range(1, len(self.unformated_history['Trades'])):

            # # Track percentage Change of AssetPrice for each position
            trade_position = self.unformated_history['Trades'][index]
            prev_trade_position = self.unformated_history['Trades'][index - 1]

            # total_cash_ballance = Simulator.PortfolioValue.calc_total_cash_value(trade_position)
            
            asset_price_change_percentage = Simulator.PortfolioValue.calc_price_change(trade_position, prev_trade_position)
            
            # knock_out = Simulator.LiquidationPrices.Binance(self.price_data, trade_position)

            # Calculate knock out price 
            # take date
            # take position size to calculate Margin
            # take leverage faktor
            # liquidation_price(self.unformated_history['Trades'][index])
            # google how knock out price is calculated

            # determine whole portfolio value for each position
            # if Positionsize is only 0.5 then find out how big is rest
            # portfolio_size(self.unformated_history['Trades'][index])                                                                                                                         65RRRRRRRRRRRRR
            

            # if ['Direction'] == 'Long':
            #     pass
            # elif ['Direction'] == 'Short':
            #     pass
            
            # element1 = self.unformated_history['Trades'][index - 1]['From']     
            # element2 = self.unformated_history['Trades'][index]['To']  
            # if element1 == 0:
            #     continue

            # # Check if this makes sense with both long and short
            # changePercentage = ((element2 / element1) - 1) * 100
            # # Multiply Percentage Change by the Leverage factor
            # change_percentage_w_leverage = changePercentage * leverage
            # # Adding a PnL key/value pair to each trade
            # self.unformated_history['Trades'][index]['PnL'] = round(changePercentage, 2)
            if trade_position['Direction'] == 'Long':
                self.unformated_history['Trades'][index]['PnL'] = round(asset_price_change_percentage, 2)
            elif trade_position['Direction'] == 'Short':
                invert_PnL = asset_price_change_percentage
                self.unformated_history['Trades'][index]['PnL'] = round( invert_PnL, 2)
            
            lol = 1