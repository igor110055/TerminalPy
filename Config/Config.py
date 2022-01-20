from DataSourceFrontend import DataSources
from AssetPairsFrontend import AssetPairs
Sources = DataSources()
# Assets = AssetPairs()

#Import Candledata
# from BinanceFetchFrontend import PriceDataFetch
# CandleSticks = PriceDataFetch()
import PriceData.BinanceFetch as BinanceFetch
CandleSticks = BinanceFetch.PriceDataFetch()

#Import Formated Price Data
from BinanceAveragePrice import AveragePrice
PriceData = AveragePrice(CandleSticks)
