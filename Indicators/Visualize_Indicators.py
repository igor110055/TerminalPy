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

def visualize_HT_TRENDLINE(PriceData,Timeframe):
    ind = Indicator.HT_TRENDLINE(PriceData,Timeframe)
    tovis = IndicatorsToFormate(ind)
    return tovis

# def visualize_KAMA(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MA(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MAMA(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MAVP(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MIDPOINT(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MIDPRICE(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_SAR(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_SAREXT(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_SMA(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_T3(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_TEMA(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_TRIMA(PriceData,Timeframe):


# visualize_WMA

#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def (PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_ADX(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_ADXR(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_APO(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_AROON(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_AROONOSC(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_BOP(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_CCI(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_CMO(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_DX(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MACD(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MACDEXT(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MACDFIX(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MFI(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MINUS_DI(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MINUS_DM(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_MOM(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_PLUS_DI(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_PLUS_DM(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_PPO(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_ROC(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_ROCP(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_ROCR(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_ROCR100(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_RSI(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_STOCH(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_STOCHF(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_STOCHRSI(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_TRIX(PriceData,Timeframe):
#     ind = Indicator.(PriceData,Timeframe)
#     tovis = IndicatorsToFormate(ind)
#     return tovis

# def visualize_ULTOSC(PriceData,Timeframe):


# visualize_WILLR
 



