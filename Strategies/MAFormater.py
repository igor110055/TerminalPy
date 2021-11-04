# import find_parent
import copy
from Indicators.getRidofNan import delNan
from DataIntegrityCheck import DataIntegrityCheck


def IndicatorsToFormate(dataSet):
    formatedIndicators = []
    # If the check is passed continue
    DataIntegrityCheck(dataSet)
    # Delete NaN Values from Indicators
    # For Every indicator Dataset we take the firs array and delete the nan Values
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


