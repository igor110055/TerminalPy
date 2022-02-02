import find_parent
import Indicators.Indicator as Indicator
from Strategies.MAFormater import IndicatorsToFormate



def visualize_SMA(PriceData,Timeframe):
    sma = Indicator.SMA(PriceData, Timeframe)
    # smatovis = visualizer(sma, PriceData, Timeframe)
    smatovis = IndicatorsToFormate(sma)
    return smatovis

# Momentum Indicators

def visualize_RSI(PriceData,Timeframe):
    rsi = Indicator.RSI(PriceData, Timeframe)
    # rsitovis = visualizer(rsi, PriceData, Timeframe)
    rsitovis = IndicatorsToFormate(rsi)
    return rsitovis

def visualize_BBANDS(PriceData,Timeframe):
    ind = Indicator.BBANDS(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_DEMA(PriceData,Timeframe):
    ind = Indicator.DEMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_EMA(PriceData,Timeframe):
    ind = Indicator.EMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_HT_TRENDLINE(PriceData):
    ind = Indicator.HT_TRENDLINE(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_KAMA(PriceData,Timeframe):
    ind = Indicator.KAMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MA(PriceData,Timeframe):
    ind = Indicator.MA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MAMA(PriceData,Timeframe):
    ind = Indicator.MAMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MAVP(PriceData,Timeframe):
    ind = Indicator.MAVP(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MIDPOINT(PriceData,Timeframe):
    ind = Indicator.MIDPOINT(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MIDPRICE(PriceData,Timeframe):
    ind = Indicator.MIDPRICE(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_SAR(PriceData,Timeframe):
    ind = Indicator.SAR(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_SAREXT(PriceData,Timeframe):
    ind = Indicator.SAREXT(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_SMA(PriceData,Timeframe):
    ind = Indicator.SMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_T3(PriceData,Timeframe):
    ind = Indicator.T3(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_TEMA(PriceData,Timeframe):
    ind = Indicator.TEMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_TRIMA(PriceData,Timeframe):
    ind = Indicator.TRIMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_WMA(PriceData,Timeframe):
    ind = Indicator.WMA(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis


#Momentum Indicators

def visualize_ADX(PriceData,Timeframe):
    ind = Indicator.ADX(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ADXR(PriceData,Timeframe):
    ind = Indicator.ADXR(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_APO(PriceData,Timeframe):
    ind = Indicator.APO(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_AROON(PriceData,Timeframe):
    ind = Indicator.AROON(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_AROONOSC(PriceData,Timeframe):
    ind = Indicator.AROONOSC(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_BOP(PriceData,Timeframe):
    ind = Indicator.BOP(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_CCI(PriceData,Timeframe):
    ind = Indicator.CCI(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_CMO(PriceData,Timeframe):
    ind = Indicator.CMO(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_DX(PriceData,Timeframe):
    ind = Indicator.DX(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MACD(PriceData,Timeframe):
    ind = Indicator.MACD(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MACDEXT(PriceData,Timeframe):
    ind = Indicator.MACDEXT(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MACDFIX(PriceData,Timeframe):
    ind = Indicator.MACDFIX(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MFI(PriceData,Timeframe):
    ind = Indicator.MFI(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MINUS_DI(PriceData,Timeframe):
    ind = Indicator.MINUS_DI(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MINUS_DM(PriceData,Timeframe):
    ind = Indicator.MINUS_DM(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_MOM(PriceData,Timeframe):
    ind = Indicator.MOM(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_PLUS_DI(PriceData,Timeframe):
    ind = Indicator.PLUS_DI(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_PLUS_DM(PriceData,Timeframe):
    ind = Indicator.PLUS_DM(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_PPO(PriceData,Timeframe):
    ind = Indicator.PRO(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ROC(PriceData,Timeframe):
    ind = Indicator.ROC(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ROCP(PriceData,Timeframe):
    ind = Indicator.ROCP(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ROCR(PriceData,Timeframe):
    ind = Indicator.ROCR(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ROCR100(PriceData,Timeframe):
    ind = Indicator.ROCR100(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_RSI(PriceData,Timeframe):
    ind = Indicator.RSI(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_STOCH(PriceData,Timeframe):
    ind = Indicator.STOCH(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_STOCHF(PriceData,Timeframe):
    ind = Indicator.STOCHF(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_STOCHRSI(PriceData,Timeframe):
    ind = Indicator.STOCHRSI(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_TRIX(PriceData,Timeframe):
    ind = Indicator.TRIX(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ULTOSC(PriceData,Timeframe):
    ind = Indicator.ULTOSC(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_WILLR(PriceData,Timeframe):
    ind = Indicator.WILLR(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis



