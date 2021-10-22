import sys

from numpy import NaN
sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
from getRidofNan import delNan

def visualize_SMA(PriceData,Timeframe):
    indicatorWithNanValues = delNan(Indicator.SMA(PriceData, Timeframe)[0])
    
    for element in PriceData:
        if PriceData.index(element) >= Timeframe:
            break
            
    to_Visualize = [indicatorWithNanValues,PriceData[0]]
    return to_Visualize