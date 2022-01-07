#Import Candledata
# import PriceData.OHLC_data_CCXT
# CandleSticks = OHLC_data_CCXT.ohlc
import PriceData.PriceDataAsJson as PriceDataAsJson
CandleSticks = PriceDataAsJson.PriceDataFetch()

#Import Formated Price Data
from PriceData.AverageWDate import AveragePrice
PriceData = AveragePrice(CandleSticks)