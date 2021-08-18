print('LOL')
import AveragePrice
import talib
Range = 50


# def Indicators(Range):
#     #Momentum Indicators

SMA = talib.SMA(AveragePrice.Average,Range)
RSI = talib.RSI(AveragePrice.Average,Range)

