import sys
sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
from getRidofNan import delNan
sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Strategies')
from MAFormater import IndicatorsToFormate

# def visualizer (Indicat0r,PriceData,Timeframe):
#     indicatorWithoutNanValues = delNan(Indicat0r[0])
    
#     for element in PriceData[0]:
#         if PriceData[0].index(element) < (Timeframe - 1):
#             PriceData[0].remove(element)
                
#     to_Visualize = {
#         'time': PriceData[0],
#         'value':[]
#     }

#     # Numbers getting Rounded
#     for element in indicatorWithoutNanValues:
#         rounded = round(element)
#         to_Visualize['value'].append(rounded)
    
#     return to_Visualize

# Overlap Studies

def visualize_SMA(PriceData,Timeframe):
    sma = Indicator.SMA(PriceData, Timeframe)
    # smatovis = visualizer(sma, PriceData, Timeframe)
    smatovis = IndicatorsToFormate(sma)
    return smatovis

# Momentum Indicators

def visualize_RSI(PriceData,Timeframe):
    rsi = Indicator.RSI(PriceData, Timeframe)
    # rsitovis = visualizer(rsi, PriceData, Timeframe)
    rsitovis = IndicatorsToFormate(rsi)
    return rsitovis