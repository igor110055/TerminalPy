import sys
sys.path.insert(1,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
import Indicator
from getRidofNan import delNan

sys.path.insert(2,'/home/hackerboi/Dokumente/python/TerminalPy/PriceData')
# import OHLC_data_CCXT
# CandleSticks = OHLC_data_CCXT.ohlc
import PriceDataAsJson
CandleSticks = PriceDataAsJson.formated

#Import Formated Price Data
from AverageWDate import AveragePrice
PriceData = AveragePrice(CandleSticks)

from DataIntegrityCheck import DataIntegrityCheck

sMA5 = Indicator.SMA(PriceData, 5)
sMA10 = Indicator.SMA(PriceData, 10)

def IndicatorsToFormate(dataSet):
    formatedIndicators = []
    #For Every indicator Dataset we take the firs array and delete the nan Values
    
    # If the check is passed continue
    DataIntegrityCheck(dataSet)
    #Delete NaN Values from Indicators
    IndicatorDataSetWithoutNaN = delNan(dataSet[0])
    
    Period = dataSet[3]
    #For Every element in the Second List of the DataSet we delete
    for element in dataSet[1]:
        if dataSet[1].index(element) < Period:
            temp = dataSet[1]
            temp.remove(element)
            # dataSet[1].remove(element)
            formatedIndicators.append(temp)

    #For Every element in the Second List of the DataSet we delete
    for element in dataSet[2]:
        if dataSet[2].index(element) <= Period:
            temp = dataSet[2]
            temp.remove(element)
            # dataSet[2].remove(element)
            formatedIndicators.append(temp)

    formatedIndicators.append([IndicatorDataSetWithoutNaN,dataSet[1],dataSet[2],dataSet[3]])
            
    return formatedIndicators

# Wenn nur eine von beiden ausgeführt wird funzt alles 
# Werden jedoch beide ausgeführt ist eine immer Falsch
# Es werden zu wenig Datum und AssetValues gepusht
# Fehler liegt wahrscheinlich zwischen line 32 und 49
# IndicatorDataSetWithoutNaN hatt immer richtig viele einträge
# Wenn nur eine Funktion ausgeführt wird DataIntegrityCheck always Passed
# Werden beide ausgeführt failt DataIntegrityCheck immer beim zweiten
IndicatorsFormated10 = IndicatorsToFormate(sMA10)
IndicatorsFormated5 = IndicatorsToFormate(sMA5)

