# def calc_total_cash_value(trade):
    
#     if trade['Direction'] == 'Long':
#         position_value = trade['From']
#         position_size = trade['PositionSize']
        
#         portfolio_value = (position_size/position_value) * 100
#         return portfolio_value

#     elif trade['Direction'] == 'Short':
#         position_value = trade['To']
#         position_size = trade['PositionSize']

#         portfolio_value = (position_size/position_value) * 100
#         return portfolio_value


def calc_price_change(trade, prev_trade):
    asset_price_position = trade['AssetPrice']
    asset_price_prev_position = prev_trade['AssetPrice']

    price_change = ((asset_price_position / asset_price_prev_position) - 1) * 100

    return round(price_change, 2)
    # if trade['Direction'] == 'Long':
    #     position_value = trade['From']
    #     position_size = trade['PositionSize']
        
    #     portfolio_value = (position_size/position_value) * 100
    #     return portfolio_value

    # elif trade['Direction'] == 'Short':
    #     position_value = trade['To']
    #     position_size = trade['PositionSize']

    #     portfolio_value = (position_size/position_value) * 100
    #     return portfolio_value
