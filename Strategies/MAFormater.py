import sys
import copy
sys.path.insert(1,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')
from getRidofNan import delNan
from DataIntegrityCheck import DataIntegrityCheck

def IndicatorToFormate(dataSet):
    # If the check is passed continue
    DataIntegrityCheck(dataSet)
    #Delete NaN Values from Indicators
    IndicatorDataSetWithoutNaN = delNan(dataSet[0])
    
    Period = dataSet[3]
    #For Every element in the Date List we delete
    TimeCopy = copy.deepcopy(dataSet[1])
    for element in TimeCopy:
        if TimeCopy.index(element) <= Period:
            TimeCopy.remove(element)

    #For Every element in the AssetValue List we delete
    AssetValueCopy = copy.deepcopy(dataSet[2])
    for element in AssetValueCopy:
        if AssetValueCopy.index(element) <= Period:
            AssetValueCopy.remove(element)
    
    formatedIndicators = {
        'value': IndicatorDataSetWithoutNaN,
        'time': TimeCopy,
        'assetValue': AssetValueCopy,
        'range': dataSet[3]
    }   
    return formatedIndicators