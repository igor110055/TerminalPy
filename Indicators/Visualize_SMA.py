import sys
sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
from getRidofNan import delNan

def visualize_SMA(PriceData,Timeframe):
    Input_SMA = Indicator.SMA(PriceData,Timeframe)
    indicatorWithoutNanValues = delNan(Input_SMA[0])

    for element in Input_SMA[1]:
        if Input_SMA[1].index(element) < (Timeframe):
            Input_SMA[1].remove(element)
      
    to_Visualize = {
        'time': Input_SMA[1],
        'value': indicatorWithoutNanValues 
    }
    
    return to_Visualize