from Config.DataSourceFrontend import DataSources
from Config.AssetPairsFrontend import AssetPairs
Sources = DataSources()
# Assets = AssetPairs()

#Import Candledata
# from BinanceFetchFrontend import PriceDataFetch
# CandleSticks = PriceDataFetch()
import PriceData.BinanceFetch as BinanceFetch
CandleSticks = BinanceFetch.PriceDataFetch()

#Import Formated Price Data
from PriceData.AverageWDate import AveragePrice
PriceData = AveragePrice(CandleSticks)
