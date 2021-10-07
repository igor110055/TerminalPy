import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/PriceData')

from AverageWDate import Average
import talib
import numpy

Price = numpy.array(Average[1])

def SMA(Range):
    _SMA = talib.SMA(Price,Range).tolist()
    #return Indicator Value, Date, and the AssetPrice
    return [_SMA,Average[0],Average[1]] 

#Momentum Indicators

def ADX(Range):
    _ADX = talib.ADX(Price,Range).tolist()
    return [_ADX,Average[0],Average[1]] 
 
def ADXR(Range):
    _ADXR = talib.ADXR(Price,Range).tolist()
    return [_ADXR,Average[0],Average[1]] 
 
def APO(Range):
    _APO = talib.APO(Price,Range).tolist()
    return [_APO,Average[0],Average[1]] 
 
def AROON(Range):
    _AROON = talib.AROON(Price,Range).tolist()
    return [_AROON,Average[0],Average[1]]
 
def AROONOSC(Range):
    _AROONOSC = talib.AROONOSC(Price,Range).tolist()
    return [_AROONOSC,Average[0],Average[1]] 
 
def BOP(Range):
    _BOP = talib.BOP(Price,Range).tolist()
    return [_BOP,Average[0],Average[1]] 
 
def CCI(Range):
    _CCI = talib.CCI(Price,Range).tolist()
    return [_CCI,Average[0],Average[1]] 
 
def CMO(Range):
    _CMO = talib.CMO(Price,Range).tolist()
    return [_CMO,Average[0],Average[1]] 
 
def DX(Range):
    _DX = talib.DX(Price,Range).tolist()
    return [_DX
,Average[0],Average[1]] 
def MACD(Range):
    _MACD = talib.MACD(Price,Range).tolist()
    return [_MACD,Average[0],Average[1]] 
 
def MACDEXT(Range):
    _MACDEXT = talib.MACDEXT(Price,Range).tolist()
    return [_MACDEXT,Average[0],Average[1]] 
 
def MACDFIX(Range):
    _MACDFIX = talib.MACDFIX(Price,Range).tolist()
    return [_MACDFIX,Average[0],Average[1]] 
 
def MFI(Range):
    _MFI = talib.MFI(Price,Range).tolist()
    return [_MFI,Average[0],Average[1]] 
 
def MINUS_DI(Range):
    _MINUS_DI = talib.MINUS_DI(Price,Range).tolist()
    return [_MINUS_DI,Average[0],Average[1]] 
 
def MINUS_DM(Range):
    _MINUS_DM = talib.MINUS_DM(Price,Range).tolist()
    return [_MINUS_DM,Average[0],Average[1]] 
 
def MOM(Range):
    _MOM = talib.MOM(Price,Range).tolist()
    return [_MOM,Average[0],Average[1]] 
 
def PLUS_DI(Range):
    _PLUS_DI = talib.PLUS_DI(Price,Range).tolist()
    return [_PLUS_DI,Average[0],Average[1]] 
 
def PLUS_DM(Range):
    _PLUS_DM = talib.PLUS_DM(Price,Range).tolist()
    return [_PLUS_DM,Average[0],Average[1]] 
 
def PPO(Range):
    _PPO = talib.PPO(Price,Range).tolist()
    return [_PPO,Average[0],Average[1]] 
 
def ROC(Range):
    _ROC = talib.ROC(Price,Range).tolist()
    return [_ROC,Average[0],Average[1]] 
 
def ROCP(Range):
    _ROCP = talib.ROCP(Price,Range).tolist()
    return [_ROCP,Average[0],Average[1]] 
 
def ROCR(Range):
    _ROCR = talib.ROCR(Price,Range).tolist()
    return [_ROCR,Average[0],Average[1]] 
 
def ROCR100(Range):
    _ROCR100 = talib.ROCR100(Price,Range).tolist()
    return [_ROCR100,Average[0],Average[1]] 

def RSI(Range):
    _RSI = talib.RSI(Price,Range).tolist()
    return [_RSI,Average[0],Average[1]] 
 
def STOCH(Range):
    _STOCH = talib.STOCH(Price,Range).tolist()
    return [_STOCH,Average[0],Average[1]] 
 
def STOCHF(Range):
    _STOCHF = talib.STOCHF(Price,Range).tolist()
    return [_STOCHF,Average[0],Average[1]] 
 
def STOCHRSI(Range):
    _STOCHRSI = talib.STOCHRSI(Price,Range).tolist()
    return [_STOCHRSI,Average[0],Average[1]] 
 
def TRIX(Range):
    _TRIX = talib.TRIX(Price,Range).tolist()
    return [_TRIX,Average[0],Average[1]] 
 
def ULTOSC(Range):
    _ULTOSC = talib.ULTOSC(Price,Range).tolist()
    return [_ULTOSC,Average[0],Average[1]] 
 
def WILLR(Range):
    _WILLR = talib.WILLR(Price,Range).tolist()
    return [_WILLR,Average[0],Average[1]] 



#Volatility Indicator
def ATR(Range):
    _ATR = talib.ATR(Price,Range).tolist()  
    return [_ATR,Average[0],Average[1]] 

def NATR(Range):
    _NATR = talib.NATR(Price,Range).tolist()
    return [_NATR,Average[0],Average[1]] 

def TRANGE(Range):
    _TRANGE = talib.TRANGE(Price,Range).tolist()
    return [_TRANGE,Average[0],Average[1]]         
                 
               