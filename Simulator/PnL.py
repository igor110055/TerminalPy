# def PnL(trade):
#     if trade['Direction'] == 'Long':
#         self.unformated_history['Trades'][index]['PnL'] = round(asset_price_change_percentage, 2)
#     elif trade['Direction'] == 'Short':
#     invert_PnL = asset_price_change_percentage
#         self.unformated_history['Trades'][index]['PnL'] = round( invert_PnL, 2)

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