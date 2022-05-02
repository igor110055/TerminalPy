# class Liquidation:

#     def __init__(self) -> None:
#         pass

# asset_price_position, date, leverage

def Binance(trade, price_data):
    
    position_value_cash_equivalent = trade
    # portfolio_value_cash_equivalent =
    asset_price_position = trade['AssetPrice']
    leverage = trade['Leverage']
    direction = trade['Direction']
    # calculate knockout price


    # Calculate knock out price 
    # take date
    # take position size to calculate Margin
    # take leverage faktor
    # liquidation_price(self.unformated_history['Trades'][index])
    # google how knock out price is calculated

    # # for every following date untill position closed check
    # date = trade['Open'] index finden in price_data
    # from index till position close(end since positions dont get closed yet)
        # for price in pricedata['Value'] range(index in price_data, len(pricedata))
        #   if price != knockout price
        #       return false
        #   elif price == knockout price
        #        return price, pricedata['date'][index]
    pass

def Kraken(self):
    pass

def Coinbase(self):
    pass

def Alpaca(self):
    pass