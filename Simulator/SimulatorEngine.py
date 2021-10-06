#Zu nem Object Umschreinben
# class Trade:

#     def __init__(self,Cash):
#         self.tradeCash = [Cash]

#     def buy(self, volatility):
#         collateral = self.tradeCash[-1]
#         VolatilityPercentage = (collateral/100)*(volatility)
#         collateral = collateral + VolatilityPercentage
#         self.tradeCash.append(collateral)
#         print(self.tradeCash)

#     def sell(self,volatility):
#         collateral = self.tradeCash[-1]
#         VolatilityPercentage = (collateral/100)*(volatility * (-1))
#         collateral = collateral + VolatilityPercentage
#         self.tradeCash.append(collateral)
#         print(self.tradeCash)




#def trade(Cash):

#tradeCash = [Cash]
tradeCash = [200]

def buy(volatility):
    collateral = tradeCash[-1]
    VolatilityPercentage = (collateral/100)*(volatility)
    collateral = collateral + VolatilityPercentage
    tradeCash.append(collateral)
    print('buy: ',tradeCash)

def sell(volatility):
    collateral = tradeCash[-1]
    VolatilityPercentage = (collateral/100)*(volatility * (-1))
    collateral = collateral + VolatilityPercentage
    tradeCash.append(collateral)
    print('sell: ',tradeCash)

