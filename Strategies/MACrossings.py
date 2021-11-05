from Strategies.MAFormater import IndicatorsToFormate
from Strategies.SortinIndicatorMINMAX import SortMAX_MIN

def SMAtoSMACompare(Indicat0r1raw, Indicator2raw):
    #Formating the Indicators Correctly(deleting all NaN Values)
    Indicat0r1 = IndicatorsToFormate(Indicat0r1raw)
    Indicator2 = IndicatorsToFormate(Indicator2raw)
    indicatorsToCompare = [Indicat0r1, Indicator2]
    # Sort Indicators from Min to Max
    mAX_mIN_Obj = SortMAX_MIN(indicatorsToCompare)
    RangeMin = mAX_mIN_Obj['RangeMin']
    RangeMax = mAX_mIN_Obj['RangeMax']
    RangeValueMin = mAX_mIN_Obj['MinValue']
    RangeValueMax = mAX_mIN_Obj['MaxValue']
    Time = mAX_mIN_Obj['Time']
    AssetValue = mAX_mIN_Obj['AssetValue']

    # Get the Difference between two MA Ranges to match the output offset
    difference = RangeMax-RangeMin

    # #Dummy Data Set
    # RangeValueMin = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    # RangeValueMax =           [9,15,20,9,9,9,11,11,11,9,9,9]

    #The Dict we return
    globalReturn = {
        'Time': [],
        'AssetValue': [],
        'MAMin': {
            'Range': RangeMin,
            'Value': []
        },
        'MAMax': {
            'Range': RangeMax,
            'Value': []
        },
        'MAonTop': []
    }

    changeWatcher = []
    #Get the difference between min and max
    difference = RangeMax - RangeMin

    for element in RangeValueMax:
        index = RangeValueMax.index(element)
        
        comp = RangeValueMin[index + difference]>RangeValueMax[index]
        changeWatcher.append(comp)

        #Make sure Changewatcher only has two entries a time
        if (len(changeWatcher) > 2):
            
            #Take away the first(left side) element 
            changeWatcher = changeWatcher[1:]
            #Listens to wether a MA Crossing occours
            if (changeWatcher[0] != changeWatcher[1]):
                #Data needs to be supplied from Indicator function
                globalReturn['Time'].append(Time[index])
                globalReturn['AssetValue'].append(round(AssetValue[index]))
                globalReturn['MAMin']['Value'].append(round(RangeValueMin[index + difference]))
                globalReturn['MAMax']['Value'].append(round(RangeValueMax[index]))
                
                #Log wich MA element is on top of the other
                if (RangeValueMin[index + difference] > RangeValueMax[index]):
                    globalReturn['MAonTop'].append(RangeMin)
                else:
                    globalReturn['MAonTop'].append(RangeMax)
                
    return globalReturn; 
