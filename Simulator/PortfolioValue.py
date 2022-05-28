def calc_total_cash_value(trade):
    position_size = trade['PositionSize']
    if position_size and trade['From'] and trade['To'] != 0:
        if trade['Direction'] == 'Long':
            position_value = trade['From']
        
            cash_not_in_position = (1 - position_size) * position_value
            portfolio_value  = position_value + cash_not_in_position
            # (position_size/position_value) * 100
            return portfolio_value

        elif trade['Direction'] == 'Short':
            position_value = trade['To']
            
            cash_not_in_position = (1 - position_size) * position_value
            portfolio_value  = position_value + cash_not_in_position
            # portfolio_value = (position_size/position_value) * 100
            return portfolio_value

def calc_total_asset_value(trade):
    position_size = trade['PositionSize']

    if trade['Direction'] == 'Long':
        position_value = trade['To']
        
        if position_size and position_value != 0:
            cash_not_in_position = (1 - position_size) * position_value
            portfolio_value  = position_value + cash_not_in_position
            # (position_size/position_value) * 100
            return portfolio_value

    elif trade['Direction'] == 'Short':
        position_value = trade['From']
        
        if position_size and position_value != 0:
            cash_not_in_position = (1 - position_size) * position_value
            portfolio_value  = position_value + cash_not_in_position
            # portfolio_value = (position_size/position_value) * 100
            return portfolio_value


def calc_price_change(trade, prev_trade):
    asset_price_position = trade['AssetPrice']
    asset_price_prev_position = prev_trade['AssetPrice']

    price_change = ((asset_price_position / asset_price_prev_position) - 1) * 100

    return round(price_change, 2)
    

def total_portfolio_value(total_cash_ammount,total_asset_ammount, asset_price):
    # conver total asset value to cash value
    asset_value_in_cash = total_asset_ammount * asset_price
    # add them both
    total_portfolio = asset_value_in_cash + total_cash_ammount
    return total_portfolio



# determine whole portfolio value for each position
# if Positionsize is only 0.5 then find out how big is rest
# portfolio_size(self.unformated_history['Trades'][index]) 