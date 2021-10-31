import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/PriceData')

import talib
import numpy

def Price(Data):
    PriceMaker = numpy.array(Data[1])
    #return Indicator Value, Date, the AssetPrice, and the Range
    return PriceMaker

def SMA(PriceDaten,Range):
    _SMA = talib.SMA(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_SMA,PriceDaten[0],PriceDaten[1],Range] 
    
#Momentum Indicators

def ADX(PriceDaten,Range):
    _ADX = talib.ADX(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADX,PriceDaten[0],PriceDaten[1],Range] 
 
def ADXR(PriceDaten,Range):
    _ADXR = talib.ADXR(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADXR,PriceDaten[0],PriceDaten[1],Range] 
 
def APO(PriceDaten,Range):
    _APO = talib.APO(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_APO,PriceDaten[0],PriceDaten[1],Range] 
 
def AROON(PriceDaten,Range):
    _AROON = talib.AROON(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_AROON,PriceDaten[0],PriceDaten[1],Range]
 
def AROONOSC(PriceDaten,Range):
    _AROONOSC = talib.AROONOSC(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_AROONOSC,PriceDaten[0],PriceDaten[1],Range] 
 
def BOP(PriceDaten,Range):
    _BOP = talib.BOP(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_BOP,PriceDaten[0],PriceDaten[1],Range] 
 
def CCI(PriceDaten,Range):
    _CCI = talib.CCI(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_CCI,PriceDaten[0],PriceDaten[1],Range] 
 
def CMO(PriceDaten,Range):
    _CMO = talib.CMO(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_CMO,PriceDaten[0],PriceDaten[1],Range] 
 
def DX(PriceDaten,Range):
    _DX = talib.DX(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_DX,PriceDaten[0],PriceDaten[1],Range] 

def MACD(PriceDaten,Range):
    _MACD = talib.MACD(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_MACD,PriceDaten[0],PriceDaten[1],Range] 
 
def MACDEXT(PriceDaten,Range):
    _MACDEXT = talib.MACDEXT(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_MACDEXT,PriceDaten[0],PriceDaten[1],Range] 
 
def MACDFIX(PriceDaten,Range):
    _MACDFIX = talib.MACDFIX(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_MACDFIX,PriceDaten[0],PriceDaten[1],Range] 
 
def MFI(PriceDaten,Range):
    _MFI = talib.MFI(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_MFI,PriceDaten[0],PriceDaten[1],Range] 
 
def MINUS_DI(PriceDaten,Range):
    _MINUS_DI = talib.MINUS_DI(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DI,PriceDaten[0],PriceDaten[1],Range] 
 
def MINUS_DM(PriceDaten,Range):
    _MINUS_DM = talib.MINUS_DM(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DM,PriceDaten[0],PriceDaten[1],Range] 
 
def MOM(PriceDaten,Range):
    _MOM = talib.MOM(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_MOM,PriceDaten[0],PriceDaten[1],Range] 
 
def PLUS_DI(PriceDaten,Range):
    _PLUS_DI = talib.PLUS_DI(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DI,PriceDaten[0],PriceDaten[1],Range] 
 
def PLUS_DM(PriceDaten,Range):
    _PLUS_DM = talib.PLUS_DM(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DM,PriceDaten[0],PriceDaten[1],Range] 
 
def PPO(PriceDaten,Range):
    _PPO = talib.PPO(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_PPO,PriceDaten[0],PriceDaten[1],Range] 
 
def ROC(PriceDaten,Range):
    _ROC = talib.ROC(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROC,PriceDaten[0],PriceDaten[1],Range] 
 
def ROCP(PriceDaten,Range):
    _ROCP = talib.ROCP(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCP,PriceDaten[0],PriceDaten[1],Range] 
 
def ROCR(PriceDaten,Range):
    _ROCR = talib.ROCR(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR,PriceDaten[0],PriceDaten[1],Range] 
 
def ROCR100(PriceDaten,Range):
    _ROCR100 = talib.ROCR100(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR100,PriceDaten[0],PriceDaten[1],Range] 

def RSI(PriceDaten,Range):
    _RSI = talib.RSI(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_RSI,PriceDaten[0],PriceDaten[1],Range] 
 
def STOCH(PriceDaten,Range):
    _STOCH = talib.STOCH(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_STOCH,PriceDaten[0],PriceDaten[1],Range] 
 
def STOCHF(PriceDaten,Range):
    _STOCHF = talib.STOCHF(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_STOCHF,PriceDaten[0],PriceDaten[1],Range] 
 
def STOCHRSI(PriceDaten,Range):
    _STOCHRSI = talib.STOCHRSI(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_STOCHRSI,PriceDaten[0],PriceDaten[1],Range] 
 
def TRIX(PriceDaten,Range):
    _TRIX = talib.TRIX(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRIX,PriceDaten[0],PriceDaten[1],Range] 
 
def ULTOSC(PriceDaten,Range):
    _ULTOSC = talib.ULTOSC(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ULTOSC,PriceDaten[0],PriceDaten[1],Range] 
 
def WILLR(PriceDaten,Range):
    _WILLR = talib.WILLR(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_WILLR,PriceDaten[0],PriceDaten[1],Range] 



#Volatility Indicator
def ATR(PriceDaten,Range):
    _ATR = talib.ATR(Price(PriceDaten),Range).tolist()  
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_ATR,PriceDaten[0],PriceDaten[1],Range] 

def NATR(PriceDaten,Range):
    _NATR = talib.NATR(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_NATR,PriceDaten[0],PriceDaten[1],Range] 

def TRANGE(PriceDaten,Range):
    _TRANGE = talib.TRANGE(Price(PriceDaten),Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRANGE,PriceDaten[0],PriceDaten[1],Range]         
                 
               