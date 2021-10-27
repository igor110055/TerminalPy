import sys

sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
from getRidofNan import delNan

def visualize_SMA(PriceData,Timeframe):
    indicatorWithoutNanValues = delNan(Indicator.SMA(PriceData, Timeframe)[0])
    
    for element in PriceData[0]:
        if PriceData[0].index(element) < (Timeframe - 1):
            PriceData[0].remove(element)
                
    to_Visualize = {
        'time': PriceData[0],
        'value':[]
    }

    # Numbers getting Rounded
    for element in indicatorWithoutNanValues:
        rounded = round(element)
        to_Visualize['value'].append(rounded)
    
    return to_Visualize