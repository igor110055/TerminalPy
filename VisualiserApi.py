import Indicators.Visualize_Indicators as Visualize_Indicators
def IndicatorGenerator(PriceData):
    Indicators = {
        'SMA5_to_Visualize' : Visualize_Indicators.visualize_SMA(PriceData, 5), 
        'SMA10_to_Visualize' : Visualize_Indicators.visualize_SMA(PriceData, 10), 
        'RSI_to_Visualize' : Visualize_Indicators.visualize_RSI(PriceData, 14)
    }
    return Indicators