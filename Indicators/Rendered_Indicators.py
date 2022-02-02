import find_parent
import Indicators.Indicator as Indicator
from Strategies.MAFormater import IndicatorsToFormate
import Indicators.Visualize_Indicators as VisIndicator


def InitSelectedIndicator(symbol,PriceData,Timeframe):
    # print(symbol,PriceData,Timeframe)
    
    # Momentum Indicators
    # if(symbol == 'BBANDS'):
    #     formated = VisIndicator.visualize_BBANDS(PriceData,Timeframe)
    #     return formated
    if(symbol == 'DEMA'):
        formated = VisIndicator.visualize_DEMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'EMA'):
        formated = VisIndicator.visualize_EMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'HT_TRENDLINE'):
        formated = VisIndicator.visualize_HT_TRENDLINE(PriceData)
        return formated
    elif(symbol == 'KAMA'):
        formated = VisIndicator.visualize_KAMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'MA'):
        formated = VisIndicator.visualize_MA(PriceData,Timeframe)
        return formated
    # elif(symbol == 'MAMA'):
    #     formated = VisIndicator.visualize_MAMA(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'MAVP'):
    #     formated = VisIndicator.visualize_MAVP(PriceData,Timeframe)
    #     return formated
    elif(symbol == 'MIDPOINT'):
        formated = VisIndicator.visualize_MIDPOINT(PriceData,Timeframe)
        return formated
    # elif(symbol == 'MIDPRICE'):
    #     formated = VisIndicator.visualize_MIDPRICE(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'SAR'):
    #     formated = VisIndicator.visualize_SAR(PriceData,Timeframe)
    #     return formated
    # elif(symbol == 'SAREXT'):
    #     formated = VisIndicator.visualize_SAREXT(PriceData,Timeframe)
    #     return formated
    elif(symbol == 'SMA'):
        formated = VisIndicator.visualize_SMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'T3'):
        formated = VisIndicator.visualize_T3(PriceData,Timeframe)
        return formated
    elif(symbol == 'TEMA'):
        formated = VisIndicator.visualize_TEMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'TRIMA'):
        formated = VisIndicator.visualize_TRIMA(PriceData,Timeframe)
        return formated
    elif(symbol == 'WMA'):
        formated = VisIndicator.visualize_WMA(PriceData,Timeframe)
        return formated
    # Momentum Indicators 
    elif(symbol == 'ADX'):
        formated = VisIndicator.visualize_ADX(PriceData,Timeframe)
        return formated
    elif(symbol == 'ADXR'):
        formated = VisIndicator.visualize_ADXR(PriceData,Timeframe)
        return formated
    elif(symbol == 'APO'):
        formated = VisIndicator.visualize_APO(PriceData,Timeframe)
        return formated
    elif(symbol == 'AROON'):
        formated = VisIndicator.visualize_AROON(PriceData,Timeframe)
        return formated
    elif(symbol == 'AROONOSC'):
        formated = VisIndicator.visualize_AROONOSC(PriceData,Timeframe)
        return formated
    elif(symbol == 'BOP'):
        formated = VisIndicator.visualize_BOP(PriceData,Timeframe)
        return formated
    elif(symbol == 'CCI'):
        formated = VisIndicator.visualize_CCI(PriceData,Timeframe)
        return formated
    elif(symbol == 'CMO'):
        formated = VisIndicator.visualize_CMO(PriceData,Timeframe)
        return formated
    elif(symbol == 'DX'):
        formated = VisIndicator.visualize_DX(PriceData,Timeframe)
        return formated
    elif(symbol == 'MACD'):
        formated = VisIndicator.visualize_MACD(PriceData,Timeframe)
        return formated
    elif(symbol == 'MACDEXT'):
        formated = VisIndicator.visualize_MACDEXT(PriceData,Timeframe)
        return formated
    elif(symbol == 'MACDFIX'):
        formated = VisIndicator.visualize_MACDFIX(PriceData,Timeframe)
        return formated
    elif(symbol == 'MFI'):
        formated = VisIndicator.visualize_MFI(PriceData,Timeframe)
        return formated
    elif(symbol == 'MINUS_DI'):
        formated = VisIndicator.visualize_MINUS_DI(PriceData,Timeframe)
        return formated
    elif(symbol == 'MINUS_DM'):
        formated = VisIndicator.visualize_MINUS_DM(PriceData,Timeframe)
        return formated
    elif(symbol == 'MOM'):
        formated = VisIndicator.visualize_MOM(PriceData,Timeframe)
        return formated
    elif(symbol == 'PLUS_DI'):
        formated = VisIndicator.visualize_PLUS_DI(PriceData,Timeframe)
        return formated
    elif(symbol == 'PLUS_DM'):
        formated = VisIndicator.visualize_PLUS_DM(PriceData,Timeframe)
        return formated
    elif(symbol == 'PPO'):
        formated = VisIndicator.visualize_PPO(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROC'):
        formated = VisIndicator.visualize_ROC(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROCP'):
        formated = VisIndicator.visualize_ROCP(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROCR'):
        formated = VisIndicator.visualize_ROCR(PriceData,Timeframe)
        return formated
    elif(symbol == 'ROCR100'):
        formated = VisIndicator.visualize_ROCR100(PriceData,Timeframe)
        return formated
    elif(symbol == 'RSI'):
        formated = VisIndicator.visualize_RSI(PriceData,Timeframe)
        return formated
    elif(symbol == 'STOCH'):
        formated = VisIndicator.visualize_STOCH(PriceData,Timeframe)
        return formated
    elif(symbol == 'STOCHF'):
        formated = VisIndicator.visualize_STOCHF(PriceData,Timeframe)
        return formated
    elif(symbol == 'STOCHRSI'):
        formated = VisIndicator.visualize_STOCHRSI(PriceData,Timeframe)
        return formated
    elif(symbol == 'TRIX'):
        formated = VisIndicator.visualize_TRIX(PriceData,Timeframe)
        return formated
    elif(symbol == 'ULTOSC'):
        formated = VisIndicator.visualize_ULTOSC(PriceData,Timeframe)
        return formated
    elif(symbol == 'WILLR'):
        formated = VisIndicator.visualize_WILLR(PriceData,Timeframe)
        return formated
        



