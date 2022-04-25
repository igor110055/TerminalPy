def calc_portfolio_value(trade):
    
    if trade['Direction'] == 'Long':
        position_value = trade['From']
        position_size = trade['PositionSize']
        
        portfolio_value = (position_size/position_value) * 100
        return portfolio_value

    elif trade['Direction'] == 'Short':
        position_value = trade['To']
        position_size = trade['PositionSize']

        portfolio_value = (position_size/position_value) * 100
        return portfolio_value

    pass