import talib
# import numpy
# from Indicators.getRidofNan import delNan

# def Data):
#     PriceMaker = numpy.array(Data[1])
#     return PriceMaker

# Overlap Studies
# # Bollinger Bands
# def BBANDS(PriceData,Range):
#     _BBANDS = talib.BBANDS(PriceData),Range)
#     Band1 = _BBANDS[0].tolist()
#     Band2 = _BBANDS[1].tolist()
#     Band3 = _BBANDS[2].tolist()
#     return[[Band1,Band2,Band3],PriceData['date'],PriceData['close'].tolist(),Range]
# Double Exponential Moving Average
def DEMA(PriceData,Range):
    _DEMA = talib.DEMA(PriceData['close'],Range).tolist()
    return[_DEMA,PriceData['date'],PriceData['close'].tolist(),Range]
# Exponential Moving Average
def EMA(PriceData,Range):
    _EMA = talib.EMA(PriceData['close'],Range).tolist()
    return[_EMA,PriceData['date'],PriceData['close'].tolist(),Range]
# # Hilbert Transform - Instantaneous Trendline
# def HT_TRENDLINE(PriceData):
#     _HT_TRENDLINE = talib.HT_TRENDLINE(PriceData['close']).tolist()
#     return[_HT_TRENDLINE,PriceData['date'],PriceData['close'].tolist()]
# Kaufman Adaptive Moving Average
def KAMA(PriceData,Range):
    _KAMA = talib.KAMA(PriceData['close'],Range).tolist()
    return[_KAMA,PriceData['date'],PriceData['close'].tolist(),Range]
# Moving average
def MA(PriceData,Range):
    _MA = talib.MA(PriceData['close'],Range).tolist()
    return[_MA,PriceData['date'],PriceData['close'].tolist(),Range]
# # MESA Adaptive Moving Average
# def MAMA(PriceData):
#     _MAMA = talib.MAMA(PriceData))
#     Trace1 = _MAMA[0].tolist()
#     Trace2 = _MAMA[1].tolist()
#     return[[Trace1,Trace2],PriceData['date'],PriceData['close'].tolist()]
# # Moving average with variable period
# def MAVP(PriceData,Range):
#     _MAVP = talib.MAVP(PriceData['close'],Range).tolist()
#     return[_MAVP,PriceData['date'],PriceData['close'].tolist(),Range]
# MidPoint over period
def MIDPOINT(PriceData,Range):
    _MIDPOINT = talib.MIDPOINT(PriceData['close'],Range).tolist()
    return[_MIDPOINT,PriceData['date'],PriceData['close'].tolist(),Range]
# Midpoint over period
def MIDPRICE(PriceData,Range):
    _MIDPRICE= talib.MIDPRICE(PriceData['high'],PriceData['low'],Range).tolist()
    return[_MIDPRICE,PriceData['date'],PriceData['close'].tolist(),Range]
# Parabolic SAR
def SAR(PriceData,Range):
    _SAR = talib.SAR(PriceData['high'],PriceData['low'],Range).tolist()
    return[_SAR,PriceData['date'],PriceData['close'].tolist(),Range]
# Parabolic SAR - Extended
def SAREXT(PriceData,Range):
    # Requires OHLC Data (high, low, Range)
    _SAREXT= talib.SAREXT(PriceData['high'],PriceData['low'],Range).tolist()
    return[_SAREXT,PriceData['date'],PriceData['close'].tolist(),Range]
# Simple Moving Average
def SMA(PriceData,Range):
    _SMA = talib.SMA(PriceData['close'],Range).tolist()
    #return Indicator Value, Date, the AssetPrice, and the Range
    return [_SMA,PriceData['date'],PriceData['close'].tolist(),Range] 
# Triple Exponential Moving Average (T3)
def T3(PriceData,Range):
    _T3 = talib.T3(PriceData['close'],Range).tolist()
    return[_T3,PriceData['date'],PriceData['close'].tolist(),Range]
# Triple Exponential Moving Average
def TEMA(PriceData,Range):
    _TEMA = talib.TEMA(PriceData['close'],Range).tolist()
    return[_TEMA,PriceData['date'],PriceData['close'].tolist(),Range]
# Triangular Moving Average
def TRIMA(PriceData,Range):
    _TRIMA = talib.TRIMA(PriceData['close'],Range).tolist()
    return[_TRIMA,PriceData['date'],PriceData['close'].tolist(),Range]
# Weighted Moving Average
def WMA(PriceData,Range):
    _WMA = talib.WMA(PriceData['close'],Range).tolist()
    return[_WMA,PriceData['date'],PriceData['close'].tolist(),Range]


    
#Momentum Indicators
# Average Directional Movement Index
def ADX(PriceData,Range):
    _ADX = talib.ADX(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADX,PriceData['date'],PriceData['close'].tolist(),Range] 
# Average Directional Movement Index Rating
def ADXR(PriceData,Range):
    _ADXR = talib.ADXR(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ADXR,PriceData['date'],PriceData['close'].tolist(),Range] 
# Absolute Price Oscillator 
# def APO(PriceData,Range):
#     _APO = talib.APO(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_APO,PriceData['date'],PriceData['close'].tolist(),Range] 
#  Aroon
def AROON(PriceData,Range):
    _AROON = talib.AROON(PriceData['high'],PriceData['low'],Range)
    aroondown = _AROON[0].tolist()
    aroonup = _AROON[1].tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [[aroondown,aroonup],PriceData['date'],PriceData['close'].tolist(),Range]
# Aroon Oscillator
def AROONOSC(PriceData,Range):
    _AROONOSC = talib.AROONOSC(PriceData['high'],PriceData['low'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_AROONOSC,PriceData['date'],PriceData['close'].tolist(),Range] 
# Balance Of Power
def BOP(PriceData):
    _BOP = talib.BOP(PriceData['open'],PriceData['high'],PriceData['low'],PriceData['close']).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_BOP,PriceData['date'],PriceData['close'].tolist()] 
# Commodity Channel Index
def CCI(PriceData,Range):
    _CCI = talib.CCI(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_CCI,PriceData['date'],PriceData['close'].tolist(),Range] 
#  Chande Momentum Oscillator
def CMO(PriceData,Range):
    _CMO = talib.CMO(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_CMO,PriceData['date'],PriceData['close'].tolist(),Range] 
#  Directional Movement Index
def DX(PriceData,Range):
    _DX = talib.DX(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_DX,PriceData['date'],PriceData['close'].tolist(),Range] 
# # Moving Average Convergence/Divergence
# def MACD(PriceData,Range):
#     _MACD = talib.MACD(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MACD,PriceData['date'],PriceData['close'].tolist(),Range] 
# # MACD with controllable MA type
# def MACDEXT(PriceData,Range):
#     _MACDEXT = talib.MACDEXT(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MACDEXT,PriceData['date'],PriceData['close'].tolist(),Range] 
# Moving Average Convergence/Divergence Fix 12/26
# def MACDFIX(PriceData,Range):
#     _MACDFIX = talib.MACDFIX(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MACDFIX,PriceData['date'],PriceData['close'].tolist(),Range] 
# # Money Flow Index 
# def MFI(PriceData,Range):
#     # Indicator requires Volume
#     _MFI = talib.MFI(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_MFI,PriceData['date'],PriceData['close'].tolist(),Range] 
# Minus Directional Indicator
def MINUS_DI(PriceData,Range):
    _MINUS_DI = talib.MINUS_DI(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DI,PriceData['date'],PriceData['close'].tolist(),Range] 
# Minus Directional Movement
def MINUS_DM(PriceData,Range):
    _MINUS_DM = talib.MINUS_DM(PriceData['high'],PriceData['low'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MINUS_DM,PriceData['date'],PriceData['close'].tolist(),Range] 
# Momentum
def MOM(PriceData,Range):
    _MOM = talib.MOM(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_MOM,PriceData['date'],PriceData['close'].tolist(),Range] 
# Plus Directional Indicator
def PLUS_DI(PriceData,Range):
    _PLUS_DI = talib.PLUS_DI(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DI,PriceData['date'],PriceData['close'].tolist(),Range] 
# Plus Directional Movement
def PLUS_DM(PriceData,Range):
    _PLUS_DM = talib.PLUS_DM(PriceData['high'],PriceData['low'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PLUS_DM,PriceData['date'],PriceData['close'].tolist(),Range] 
# Percentage Price Oscillator
def PPO(PriceData,Range):
    _PPO = talib.PPO(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_PPO,PriceData['date'],PriceData['close'].tolist(),Range] 
# Rate of change : ((price/prevPrice)-1)*100
def ROC(PriceData,Range):
    _ROC = talib.ROC(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROC,PriceData['date'],PriceData['close'].tolist(),Range] 
# Rate of change Percentage: (price-prevPrice)/prevPrice
def ROCP(PriceData,Range):
    _ROCP = talib.ROCP(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCP,PriceData['date'],PriceData['close'].tolist(),Range] 
# Rate of change ratio: (price/prevPrice)
def ROCR(PriceData,Range):
    _ROCR = talib.ROCR(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR,PriceData['date'],PriceData['close'].tolist(),Range] 
# Rate of change ratio 100 scale: (price/prevPrice)*100
def ROCR100(PriceData,Range):
    _ROCR100 = talib.ROCR100(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ROCR100,PriceData['date'],PriceData['close'].tolist(),Range] 
# Relative Strength Index
def RSI(PriceData,Range):
    _RSI = talib.RSI(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_RSI,PriceData['date'],PriceData['close'].tolist(),Range] 
# # Stochastic
# def STOCH(PriceData,Range):
#     _STOCH = talib.STOCH(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_STOCH,PriceData['date'],PriceData['close'].tolist(),Range] 
# # Stochastic Fast
# def STOCHF(PriceData,Range):
#     _STOCHF = talib.STOCHF(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_STOCHF,PriceData['date'],PriceData['close'].tolist(),Range] 
# Stochastic Relative Strength Index
# def STOCHRSI(PriceData,Range):
#     _STOCHRSI = talib.STOCHRSI(PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_STOCHRSI,PriceData['date'],PriceData['close'].tolist(),Range] 
#  1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
def TRIX(PriceData,Range):
    _TRIX = talib.TRIX(PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRIX,PriceData['date'],PriceData['close'].tolist(),Range] 
# # Ultimate Oscillator
# def ULTOSC(PriceData,Range):
#     # Indicator requires 3 Ranges
#     _ULTOSC = talib.ULTOSC(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
#     ##return Indicator Value, Date, the AssetPrice, and the Range
#     return [_ULTOSC,PriceData['date'],PriceData['close'].tolist(),Range] 
 
def WILLR(PriceData,Range):
    _WILLR = talib.WILLR(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_WILLR,PriceData['date'],PriceData['close'].tolist(),Range] 



# # Volume Indicators
# # They Obv need Volume

# def AD(PriceData):
#     _AD = talib.AD(PriceData['high'],PriceData['low'],PriceData['close']).tolist()
#     return[_AD,PriceData['date'],PriceData['close'].tolist()]

# def ADOSC(PriceData):
#     _ADOSC = talib.ADOSC(PriceData['high'],PriceData['low'],PriceData['close']).tolist()
#     return[_ADOSC,PriceData['date'],PriceData['close'].tolist()]

# def OBV(PriceData):
#     _OBV = talib.OBV(PriceData['close']).tolist()
#     return[_OBV,PriceData['date'],PriceData['close'].tolist()]



# Cycle Indicators
# Hilbert Transform - Dominant Cycle Period
def HT_DCPERIOD(PriceData):
    _HT_DCPERIOD = talib.HT_DCPERIOD(PriceData['close']).tolist()
    return[_HT_DCPERIOD,PriceData['date'],PriceData['close'].tolist()]
# Hilbert Transform - Dominant Cycle Phase
def HT_DCPHASE(PriceData):
    _HT_DCPHASE = talib.HT_DCPHASE(PriceData['close']).tolist()
    return[_HT_DCPHASE,PriceData['date'],PriceData['close'].tolist()]
# Hilbert Transform - Phasor Components
def HT_PHASOR(PriceData):
    _HT_PHASOR = talib.HT_PHASOR(PriceData['close']).tolist()
    return[_HT_PHASOR,PriceData['date'],PriceData['close'].tolist()]
# Hilbert Transform - SineWave
def HT_SINE(PriceData):
    _HT_SINE = talib.HT_SINE(PriceData['close']).tolist()
    return[_HT_SINE,PriceData['date'],PriceData['close'].tolist()]
# Hilbert Transform - Trend vs Cycle Mode
def HT_TRENDMODE(PriceData):
    _HT_TRENDMODE = talib.HT_TRENDMODE(PriceData['close']).tolist()
    return[_HT_TRENDMODE,PriceData['date'],PriceData['close'].tolist()]


#Volatility Indicators
# Average True Range
def ATR(PriceData,Range):
    _ATR = talib.ATR(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()  
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_ATR,PriceData['date'],PriceData['close'].tolist(),Range] 
# Normalized Average True Range
def NATR(PriceData,Range):
    _NATR = talib.NATR(PriceData['high'],PriceData['low'],PriceData['close'],Range).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_NATR,PriceData['date'],PriceData['close'].tolist(),Range] 
# True Range
def TRANGE(PriceData,Range):
    _TRANGE = talib.TRANGE(PriceData['high'],PriceData['low'],PriceData['close']).tolist()
    ##return Indicator Value, Date, the AssetPrice, and the Range
    return [_TRANGE,PriceData['date'],PriceData['close'].tolist()]         



# Statistic Functions(PriceData,Range):
# Beta
def BETA(PriceData,Range):
    _BETA = talib.BETA(PriceData['high'],PriceData['low'],Range).tolist()
    return [_BETA,PriceData['date'],PriceData['close'].tolist(),Range]
# Pearson's Correlation Coefficient (r)
def CORREL(PriceData,Range):
    _CORREL = talib.CORREL(PriceData['high'],PriceData['low'],Range).tolist()
    return [_CORREL,PriceData['date'],PriceData['close'].tolist(),Range]
# Linear Regression
def LINEARREG(PriceData,Range):
    _LINEARREG = talib.LINEARREG(PriceData['close'],Range).tolist()
    return [_LINEARREG,PriceData['date'],PriceData['close'].tolist(),Range]
# Linear Regression Angle
def LINEARREG_ANGLE(PriceData,Range):
    _LINEARREG_ANGLE = talib.LINEARREG_ANGLE(PriceData['close'],Range).tolist()
    return [_LINEARREG_ANGLE,PriceData['date'],PriceData['close'].tolist(),Range]
# Linear Regression Intercept
def LINEARREG_INTERCEPT(PriceData,Range):
    _LINEARREG_INTERCEPT = talib.LINEARREG_INTERCEPT(PriceData['close'],Range).tolist()
    return [_LINEARREG_INTERCEPT,PriceData['date'],PriceData['close'].tolist(),Range]
# Linear Regression Slope
def LINEARREG_SLOPE(PriceData,Range):
    _LINEARREG_SLOPE = talib.LINEARREG_SLOPE(PriceData['close'],Range).tolist()
    return [_LINEARREG_SLOPE,PriceData['date'],PriceData['close'].tolist(),Range]
# Standard Deviation
def STDDEV(PriceData,Range):
    _STDDEV = talib.STDDEV(PriceData['close'],Range).tolist()
    return [_STDDEV,PriceData['date'],PriceData['close'].tolist(),Range]
# Time Series Forecast
def TSF(PriceData,Range):
    _TSF = talib.TSF(PriceData['close'],Range).tolist()
    return [_TSF,PriceData['date'],PriceData['close'].tolist(),Range]
# Variance
def VAR(PriceData,Range):
    _VAR= talib.VAR(PriceData['close'],Range).tolist()
    return [_VAR,PriceData['date'],PriceData['close'].tolist(),Range]  


# Math Transform

def ACOS(PriceData):
    _ACOS = talib.ACOS(PriceData['close']).tolist()
    return [_ACOS,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric ACos
def ASIN(PriceData):
    _ASIN = talib.ASIN(PriceData['close']).tolist()
    return [_ASIN,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric ASin
def ATAN(PriceData):
    _ATAN = talib.ATAN(PriceData['close']).tolist()
    return [_ATAN,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric ATan
def CEIL(PriceData):
    _CEIL = talib.CEIL(PriceData['close']).tolist()
    return [_CEIL,PriceData['date'],PriceData['close'].tolist()]

# Vector Ceil
def COS(PriceData):
    _COS = talib.COS(PriceData['close']).tolist()
    return [_COS,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric Cos
def COSH(PriceData):
    _COSH = talib.COSH(PriceData['close']).tolist()
    return [_COSH,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric Cosh
def EXP(PriceData):
    _EXP = talib.EXP(PriceData['close']).tolist()
    return [_EXP,PriceData['date'],PriceData['close'].tolist()]

# Vector Arithmetic Exp
def FLOOR(PriceData):
    _FLOOR = talib.FLOOR(PriceData['close']).tolist()
    return [_FLOOR,PriceData['date'],PriceData['close'].tolist()]

# Vector Floor
def LN(PriceData):
    _LN = talib.LN(PriceData['close']).tolist()
    return [_LN,PriceData['date'],PriceData['close'].tolist()]

# Vector Log Natural
def LOG10(PriceData):
    _LOG10 = talib.LOG10(PriceData['close']).tolist()
    return [_LOG10,PriceData['date'],PriceData['close'].tolist()]

# Vector Log10
def SIN(PriceData):
    _SIN = talib.SIN(PriceData['close']).tolist()
    return [_SIN,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric Sin
def SINH(PriceData):
    _SINH = talib.SINH(PriceData['close']).tolist()
    return [_SINH,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric Sinh
def SQRT(PriceData):
    _SQRT = talib.SQRT(PriceData['close']).tolist()
    return [_SQRT,PriceData['date'],PriceData['close'].tolist()]

# Vector Square Root
def TAN(PriceData):
    _TAN = talib.TAN(PriceData['close']).tolist()
    return [_TAN,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric Tan
def TANH(PriceData):
    _TANH = talib.TANH(PriceData['close']).tolist()
    return [_TANH,PriceData['date'],PriceData['close'].tolist()]

# Vector Trigonometric Tanh



# Math Operators

def ADD(PriceData):
    _ADD = talib.ADD(PriceData['high'],PriceData['low']).tolist()
    return [_ADD,PriceData['date'],PriceData['close'].tolist()]
# Vector Arithmetic Add
def DIV(PriceData):
    _DIV = talib.DIV(PriceData['high'],PriceData['low']).tolist()
    return [_DIV,PriceData['date'],PriceData['close'].tolist()]
# Vector Arithmetic Div
def MAX(PriceData,Range):
    _MAX = talib.MAX(PriceData['close'],Range).tolist()
    return [_MAX,PriceData['date'],PriceData['close'].tolist(),Range]
# Highest value over a specified period
def MAXINDEX(PriceData,Range):
    _MAXINDEX = talib.MAXINDEX(PriceData['close'],Range).tolist()
    return [_MAXINDEX,PriceData['date'],PriceData['close'].tolist(),Range]
# Index of highest value over a specified period
def MIN(PriceData,Range):
    _MIN = talib.MIN(PriceData['close'],Range).tolist()
    return [_MIN,PriceData['date'],PriceData['close'].tolist(),Range]
# Lowest value over a specified period
def MININDEX(PriceData,Range):
    _MININDEX = talib.MININDEX(PriceData['close'],Range).tolist()
    return [_MININDEX,PriceData['date'],PriceData['close'].tolist(),Range]
# Index of lowest value over a specified period
def MINMAX(PriceData,Range):
    _MINMAX = talib.MINMAX(PriceData['close'],Range).tolist()
    return [_MINMAX,PriceData['date'],PriceData['close'].tolist(),Range]
# Lowest and highest values over a specified period
def MINMAXINDEX(PriceData,Range):
    _MINMAXINDEX = talib.MINMAXINDEX(PriceData['close'],Range).tolist()
    return [_MINMAXINDEX,PriceData['date'],PriceData['close'].tolist(),Range]
# Indexes of lowest and highest values over a specified period
def MULT(PriceData):
    _MULT = talib.MULT(PriceData['high'],PriceData['low']).tolist()
    return [_MULT,PriceData['date'],PriceData['close'].tolist()]
# Vector Arithmetic Mult
def SUB(PriceData):
    _SUB = talib.SUB(PriceData['high'],PriceData['low']).tolist()
    return [_SUB,PriceData['date'],PriceData['close'].tolist()]
# Vector Arithmetic Substraction
def SUM(PriceData,Range):
    _SUM = talib.SUM(PriceData['close'],Range).tolist()
    return [_SUM,PriceData['date'],PriceData['close'].tolist(),Range]                  
# Summation