import sys
sys.path.insert(1,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator

sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/PriceData')
import PriceDataAsJson
CandleSticks = PriceDataAsJson.formated

#Import Formated Price Data
from AverageWDate import AveragePrice
PriceData = AveragePrice(CandleSticks)

sMA5 = Indicator.SMA(PriceData, 5)
sMA10 = Indicator.SMA(PriceData, 10)

from MAFormater import IndicatorToFormate

test5 = IndicatorToFormate(sMA5)
test10 = IndicatorToFormate(sMA10)