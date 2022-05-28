# class Liquidation:

#     def __init__(self) -> None:
#         pass

# asset_price_position, date, leverage
def Test(trade):

    # Calculate knock out price 
    # take date
    # take position size to calculate Margin
    # take leverage leverage_factor
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


    # position_value_cash_equivalent = trade[]
    # portfolio_value_cash_equivalent = trade[]
    asset_price_position_entry = trade['AssetPrice']
    leverage_factor = trade['Leverage']
    direction = trade['Direction']

    price = 0

    if direction == 'Long':
        tradecollateral = trade['From']
    if direction == 'Short':
        tradecollateral = trade['To']
    
    accountballance = trade['TotalPortfolioValue']
   
    
    schwankungAbsolut = price - asset_price_position_entry
    schwankung = ((price / asset_price_position_entry) - 1) * 100

    leverage = tradecollateral * leverage_factor

    profitloss = 0

    liquidationlevel = 0

    if direction == 'Long':
        # profitloss = (leverage / 100) * schwankung
        liquidationlevel = ((0.8 * tradecollateral) - accountballance) / (leverage / 100)
    elif direction == 'Short':
        # profitloss = (leverage / 100) * (-schwankung)
        liquidationlevel = (-((0.8 * tradecollateral) - accountballance) / (leverage / 100))


    # equity = accountballance + profitloss
    # marginlevel = (equity / tradecollateral) * 100
    liquidationpreis = asset_price_position_entry-((-liquidationlevel * 0.01)*asset_price_position_entry)
    
    return liquidationpreis

def Binance(trade):
    pass

def Kraken(self):
    pass

def Coinbase(self):
    pass

def Alpaca(self):
    pass