# Api that will be fetched to Visualize Indicators and CandleStick Data exclusevly
# from Config.DataSourceFrontend import DataSources
# from Config.AssetPairsFrontend import AssetPairs
import Indicators.Visualize_Indicators as Visualize_Indicators
from Server.VisualiserServer import Server as VisServer
from Config.Config import Sources, CandleSticks, PriceData

# Sources = DataSources()
# Assets = AssetPairs()

SMA5_to_Visualize = Visualize_Indicators.visualize_SMA(PriceData, 5) 
SMA10_to_Visualize = Visualize_Indicators.visualize_SMA(PriceData, 10) 
RSI_to_Visualize = Visualize_Indicators.visualize_RSI(PriceData, 14)

VisServer(
    Sources,
    CandleSticks,
    [SMA10_to_Visualize, SMA5_to_Visualize, RSI_to_Visualize]
)
