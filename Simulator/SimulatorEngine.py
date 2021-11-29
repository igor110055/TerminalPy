# List Cannot be empty, if no Asset or no Cash just insert 0
Cash = [0]
Asset = [0.01]

def sell(price):
    collateral = Asset[-1]
    if collateral == 0:
        print('Cant sell')
    else:
        CashAmount = round(collateral*price, 2)
        Cash.append(CashAmount)

def buy(price):
    collateral = Cash[-1]
    if collateral == 0:
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
