TradeCash = [200]

def buy(volatility):
    collateral = TradeCash[-1]
    VolatilityPercentage = (collateral/100)*(volatility)
    collateral = collateral + VolatilityPercentage
    TradeCash.append(collateral)


def sell(volatility):
    collateral = TradeCash[-1]
    VolatilityPercentage = (collateral/100)*(volatility * (-1))
    collateral = collateral + VolatilityPercentage
    TradeCash.append(collateral)
  

#Zu nem Object Umschreinben
# class Trade:

#     def __init__(self,Cash):
#         self.TradeCash = [Cash]

#     def buy(self, volatility):
#         collateral = self.TradeCash[-1]
#         VolatilityPercentage = (collateral/100)*(volatility)
#         collateral = collateral + VolatilityPercentage
#         self.TradeCash.append(collateral)
#         print(self.TradeCash)#TradeData['AssetValue'].append

#     def sell(self,volatility):
#         collateral = self.TradeCash[-1]
#         VolatilityPercentage = (collateral/100)*(volatility * (-1))
#         collateral = collateral + VolatilityPercentage
#         self.TradeCash.append(collateral)
#         print(self.TradeCash)#TradeData['AssetValue'].append



