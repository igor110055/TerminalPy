import math
from AveragePrice import Average
from OHLC_data import ohlc
import talib



def SMA(Range):
    _SMA = talib.SMA(Average,Range).tolist() 
    return _SMA

#Momentum Indicators

def ADX(Range):
    _ADX = talib.ADX(Average,Range).tolist()
    return _ADX
 
def ADXR(Range):
    _ADXR = talib.ADXR(Average,Range).tolist()
    return _ADXR
 
def APO(Range):
    _APO = talib.APO(Average,Range).tolist()
    return _APO
 
def AROON(Range):
    _AROON = talib.AROON(Average,Range).tolist()
    return _AROON
 
def AROONOSC(Range):
    _AROONOSC = talib.AROONOSC(Average,Range).tolist()
    return _AROONOSC
 
def BOP(Range):
    _BOP = talib.BOP(Average,Range).tolist()
    return _BOP
 
def CCI(Range):
    _CCI = talib.CCI(Average,Range).tolist()
    return _CCI
 
def CMO(Range):
    _CMO = talib.CMO(Average,Range).tolist()
    return _CMO
 
def DX(Range):
    _DX = talib.DX(Average,Range).tolist()
    return _DX

def MACD(Range):
    _MACD = talib.MACD(Average,Range).tolist()
    return _MACD
 
def MACDEXT(Range):
    _MACDEXT = talib.MACDEXT(Average,Range).tolist()
    return _MACDEXT
 
def MACDFIX(Range):
    _MACDFIX = talib.MACDFIX(Average,Range).tolist()
    return _MACDFIX
 
def MFI(Range):
    _MFI = talib.MFI(Average,Range).tolist()
    return _MFI
 
def MINUS_DI(Range):
    _MINUS_DI = talib.MINUS_DI(Average,Range).tolist()
    return _MINUS_DI
 
def MINUS_DM(Range):
    _MINUS_DM = talib.MINUS_DM(Average,Range).tolist()
    return _MINUS_DM
 
def MOM(Range):
    _MOM = talib.MOM(Average,Range).tolist()
    return _MOM
 
def PLUS_DI(Range):
    _PLUS_DI = talib.PLUS_DI(Average,Range).tolist()
    return _PLUS_DI
 
def PLUS_DM(Range):
    _PLUS_DM = talib.PLUS_DM(Average,Range).tolist()
    return _PLUS_DM
 
def PPO(Range):
    _PPO = talib.PPO(Average,Range).tolist()
    return _PPO
 
def ROC(Range):
    _ROC = talib.ROC(Average,Range).tolist()
    return _ROC
 
def ROCP(Range):
    _ROCP = talib.ROCP(Average,Range).tolist()
    return _ROCP
 
def ROCR(Range):
    _ROCR = talib.ROCR(Average,Range).tolist()
    return _ROCR
 
def ROCR100(Range):
    _ROCR100 = talib.ROCR100(Average,Range).tolist()
    return _ROCR100

def RSI(Range):
    _RSI = talib.RSI(Average,Range).tolist()
    return _RSI
 
def STOCH(Range):
    _STOCH = talib.STOCH(Average,Range).tolist()
    return _STOCH
 
def STOCHF(Range):
    _STOCHF = talib.STOCHF(Average,Range).tolist()
    return _STOCHF
 
def STOCHRSI(Range):
    _STOCHRSI = talib.STOCHRSI(Average,Range).tolist()
    return _STOCHRSI
 
def TRIX(Range):
    _TRIX = talib.TRIX(Average,Range).tolist()
    return _TRIX
 
def ULTOSC(Range):
    _ULTOSC = talib.ULTOSC(Average,Range).tolist()
    return _ULTOSC
 
def WILLR(Range):
    _WILLR = talib.WILLR(Average,Range).tolist()
    return _WILLR



#Volatility Indicator
def ATR(Range):
    _ATR = talib.ATR(Average,Range).tolist()  
    return _ATR

def NATR(Range):
    _NATR = talib.NATR(Average,Range).tolist()
    return _NATR

def TRANGE(Range):
    _TRANGE = talib.TRANGE(Average,Range).tolist()
    return _TRANGE         
                 
               