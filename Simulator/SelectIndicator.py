import find_parent
import Indicators.Indicator as Indicator
from Strategies.MAFormater import IndicatorsToFormate


def InitSelectedIndicator(symbol,PriceData,Timeframe):
    # print(symbol,PriceData,Timeframe)
    
    # Momentum Indicators
    # if(symbol == 'BBANDS'):
    #     formated = Indicator.BBANDS(PriceData,Timeframe)
    #     return formated
    if(symbol == 'DEMA'):
        formated = Indicator.DEMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'EMA'):
        formated = Indicator.EMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'HT_TRENDLINE'):
        formated = Indicator.HT_TRENDLINE(PriceData)
        return formated
    elif(symbol == 'KAMA'):
        formated = Indicator.KAMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'MA'):
        formated = Indicator.MA(PriceData,Timeframe)
        return formated
    # elif(symbol == 'MAMA'):
    #     formated = Indicator.MAMA(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'MAVP'):
    #     formated = Indicator.MAVP(PriceData,Timeframe)
    #     return formated
    elif(symbol == 'MIDPOINT'):
        formated = Indicator.MIDPOINT(PriceData,Timeframe)
        return formated
    # elif(symbol == 'MIDPRICE'):
    #     formated = Indicator.MIDPRICE(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'SAR'):
    #     formated = Indicator.SAR(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'SAREXT'):
    #     formated = Indicator.SAREXT(PriceData,Timeframe)
    #     return formated
    elif(symbol == 'SMA'):
        formated = Indicator.SMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'T3'):
        formated = Indicator.T3(PriceData,Timeframe)
        return formated
    elif(symbol == 'TEMA'):
        formated = Indicator.TEMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'TRIMA'):
        formated = Indicator.TRIMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'WMA'):
        formated = Indicator.WMA(PriceData,Timeframe)
        return formated
