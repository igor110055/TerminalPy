import find_parent
import Indicators.Indicator as Indicator
from Strategies.MAFormater import IndicatorsToFormate


# Overlap Studies

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

def visualize_RSI(PriceData,Timeframe):
    rsi = Indicator.RSI(PriceData, Timeframe)
    rsitovis = IndicatorsToFormate(rsi)
    return rsitovis

def visualize_SMA(PriceData,Timeframe):
    sma = Indicator.SMA(PriceData, Timeframe)
    smatovis = IndicatorsToFormate(sma)
    return smatovis

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

def visualize_BOP(PriceData):
    ind = Indicator.BOP(PriceData)
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

 # Volume Indicators

def visualize_AD(PriceData):
    ind =Indicator.AD(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_ADOSC(PriceData):
    ind =Indicator.ADOSC(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_OBV(PriceData):
    ind =Indicator.OBV(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

#Volatility Indicators

def visualize_ATR(PriceData,Range):
    ind = Indicator.ATR(PriceData, Range) 
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_NATR(PriceData,Range):
    ind = Indicator.NATR(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_TRANGE(PriceData,Range):
    ind = Indicator.TRANGE(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis

# Cycle Indicators

def visualize_HT_DCPERIOD(PriceData):
    ind = Indicator.HT_DCPERIOD(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_HT_DCPHASE(PriceData):
    ind = Indicator.HT_DCPHASE(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_HT_PHASOR(PriceData):
    ind = Indicator.HT_PHASOR(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_HT_SINE(PriceData):
    ind = Indicator.HT_SINE(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_HT_TRENDMODE(PriceData):
    ind = Indicator.HT_TRENDMODE(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

# Statistic Functions:

def visualize_BETA(PriceData,Range):
    ind = Indicator.BETA(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_CORREL(PriceData,Range):
    ind = Indicator.CORREL(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_LINEARREG(PriceData,Range):
    ind = Indicator.LINEARREG(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_LINEARREG_ANGLE(PriceData,Range):
    ind = Indicator.LINEARREG_ANGLE(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_LINEARREG_INTERCEPT(PriceData,Range):
    ind = Indicator.LINEARREG_INTERCEPT(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_LINEARREG_SLOPE(PriceData,Range):
    ind = Indicator.LINEARREG_SLOPE(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_STDDEV(PriceData,Range):
    ind = Indicator.STDDEV(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_TSF(PriceData,Range):
    ind = Indicator.TSF(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_VAR(PriceData,Range):
    ind = Indicator.VA(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis

# Math Transform

def visualize_ACOS(PriceData):
    ind = Indicator.ACOS(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ASIN(PriceData):
    ind = Indicator.ASIN(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_ATAN(PriceData):
    ind = Indicator.ATAN(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_CEIL(PriceData):
    ind = Indicator.CEIL(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
   
def visualize_COS(PriceData):
    ind = Indicator.COS(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_COSH(PriceData):
    ind = Indicator.COSH(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_EXP(PriceData):
    ind = Indicator.EXP(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_FLOOR(PriceData):
    ind = Indicator.FLOOR(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_LN(PriceData):
    ind = Indicator.LN(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_LOG10(PriceData):
    ind = Indicator.LOG10(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_SIN(PriceData):
    ind = Indicator.SIN(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_SINH(PriceData):
    ind = Indicator.SINH(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_SQRT(PriceData):
    ind = Indicator.SQRT(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_TAN(PriceData):
    ind = Indicator.TAN(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_TANH(PriceData):
    ind = Indicator.TANH(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

# Math Operators

def visualize_ADD(PriceData):
    ind = Indicator.ADD(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_DIV(PriceData):
    ind = Indicator.DIV(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_MAX(PriceData,Range):
    ind = Indicator.MAX(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    

def visualize_MAXINDEX(PriceData,Range):
    ind = Indicator.MAXINDEX(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_MIN(PriceData,Range):
    ind = Indicator.MIN(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_MININDEX(PriceData,Range):
    ind = Indicator.MININDEX(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_MINMAX(PriceData,Range):
    ind = Indicator.MINMAX(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_MINMAXINDEX(PriceData,Range):
    ind = Indicator.MINMAXINDEX(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_MULT(PriceData):
    ind = Indicator.MULT(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis
    
def visualize_SUB(PriceData):
    ind = Indicator.SUB(PriceData)
    tovis = IndicatorsToFormate(ind)
    return tovis

def visualize_SUM(PriceData,Range):
    ind = Indicator.SUM(PriceData, Range)
    tovis = IndicatorsToFormate(ind)
    return tovis