from AverageWDate import Average
from OHLC_data_CCXT import ohlc
import talib
import numpy

Price = numpy.array(Average[1])

def SMA(Range):
    _SMA = talib.SMA(Price,Range).tolist()
    #retturn a list with Indicator Value, Date, and the AssetPrice
    return [_SMA,Average[0],Average[1]]


# print(SMA(30))