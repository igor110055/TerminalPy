# Api that will be fetched to Visualize Indicators and CandleStick Data exclusevly
import Indicators.Visualize_Indicators as Visualize_Indicators
from Server.VisualiserServer import Server
from Config import PriceData
from Config import CandleSticks

SMA5_to_Visualize = Visualize_Indicators.visualize_SMA(PriceData, 5) 
SMA10_to_Visualize = Visualize_Indicators.visualize_SMA(PriceData, 10) 
RSI_to_Visualize = Visualize_Indicators.visualize_RSI(PriceData, 14)

Server(CandleSticks, [SMA10_to_Visualize, SMA5_to_Visualize])