from AverageWDate import Average
from OHLC_data import ohlc
import talib


def SMA(Range):
    _SMA = talib.SMA(Average[1],Range).tolist() 
    return _SMA

print(SMA(30))