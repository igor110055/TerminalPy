from OHLC_data import ohlc
import math

def AppendDatePrice(IndicatorData):
    Output = {
    'Time':[],
    'AssetPrice':[],
    'IndicatorValue':[]
    }

    for element in IndicatorData:
        if math.isnan(element) == True:
            Output['IndicatorValue'].append(0)
        else:
            Output['IndicatorValue'].append(element)

    for element in ohlc:
        Output['Time'].append(element[0])
        Output['AssetPrice'].append(element[4])

    return Output
