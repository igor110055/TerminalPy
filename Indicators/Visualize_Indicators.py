import sys
sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/Strategies')
from MAFormater import IndicatorsToFormate

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