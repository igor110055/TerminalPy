#Import Candledata
# import PriceData.OHLC_data_CCXT
# CandleSticks = OHLC_data_CCXT.ohlc
import PriceData.BinanceFetch as BinanceFetch
CandleSticks = BinanceFetch.PriceDataFetch()

#Import Formated Price Data
from PriceData.AverageWDate import AveragePrice
PriceData = AveragePrice(CandleSticks)
