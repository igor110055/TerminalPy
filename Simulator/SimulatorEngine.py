# So in this Case before we start trading, imagine we have a Brokerage Account
# with no Cash, but with only 0.1 Bitcoin as our Ballange to start with

# List Cannot be empty, if no Asset or no Cash just insert 0
Cash = [0]
Asset = [0.01]

def sell(price):
    collateral = Asset[-1]
    if collateral == 0:
        # If the first Trade that our Bot would make would be a Sell we could not 
        # execute that if we would not have Bitcoin in our Account
        # But in our Scenrio thats not going to happen

        print('Cant sell')
    else:
        CashAmount = round(collateral*price, 2)
        Cash.append(CashAmount)

def buy(price):
    collateral = Cash[-1]
    if collateral == 0:
        # If the first Trade that our Bot would make would be a buy we obviously cannot 
        # execute that since we have no Cash in our Account
        print('Cant buy')
    else:
        AssetAmount = round(collateral/price, 8)
        Asset.append(AssetAmount)



# TradeCash = [200]

# def buy(volatility):
#     collateral = TradeCash[-1]
#     VolatilityPercentage = (collateral/100)*(volatility)
#     collateral = collateral + VolatilityPercentage
#     TradeCash.append(collateral)


# def sell(volatility):
#     collateral = TradeCash[-1]
#     VolatilityPercentage = (collateral/100)*(volatility * (-1))
#     collateral = collateral + VolatilityPercentage
#     TradeCash.append(collateral)
