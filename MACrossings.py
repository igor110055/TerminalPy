#from math import log
import IndicatorWDate
from getRidofNan import delNan
#from AppendDatePrice import AppendDatePrice

def SMAtoSMACompare(MARange1, MARange2):
    #Compare two MA Ranges and filtering the min and max value
    RangeMin = min(MARange1, MARange2)
    RangeMax = max(MARange1, MARange2)

    # #Dummy Data Set
    # RangeValueMin = [1,2,3,4,5,10,10,10,10,10,10,10,10,10,10,10,10]
    # RangeValueMax =           [10,15,20,9,9,9,11,11,11,9,8,7]

    #Get historical MA Values 
    #and deleting all nan values from the data list
    RangeValueMinWnan = IndicatorWDate.SMA(RangeMin)
    RangeValueMin = delNan(RangeValueMinWnan[0])
    
    RangeValueMaxWnan = IndicatorWDate.SMA(RangeMax)
    RangeValueMax = delNan(RangeValueMaxWnan[0])
    # RangeValueMin = AppendDatePrice( delNan (IndicatorWDate.SMA(RangeMin) ) )
    # RangeValueMax = AppendDatePrice( delNan (IndicatorWDate.SMA(RangeMax) ) )

    #The Dict we return
    globalReturn = {
        'time': [],
        'AssetValue': [],
        'MAMin': {
            'Range': RangeMin,
            'value': []
        },
        'MAMax': {
            'Range': RangeMax,
            'value': []
        },
        'MAonTop': []
    }

    changeWatcher = []
    #Get the difference between min and max
    difference = (max(MARange1, MARange2)-min(MARange1, MARange2))

    for element in RangeValueMax:
        ind = RangeValueMax.index(element)
        
        comp = RangeValueMin[ind + difference]>RangeValueMax[ind]
        changeWatcher.append(comp)
        #Make sure Changewatcher only has two entries a time
        if (len(changeWatcher) > 2):
            
            #Take away the first(left side) element 
            changeWatcher = changeWatcher[1:]
            #Listens to wether a MA Crossing occours
            if (changeWatcher[0] != changeWatcher[1]):
                #Data needs to be supplied from Indicator function
                globalReturn['time'].append(RangeValueMaxWnan[1][ind + difference])
                globalReturn['AssetValue'].append(RangeValueMaxWnan[2][ind + difference])
                
                globalReturn['MAMin']['value'].append(RangeValueMin[ind + difference])
                globalReturn['MAMax']['value'].append(RangeValueMax[ind])
                
                #Log wich MA element is on top of the other
                if (RangeValueMin[ind + difference] > RangeValueMax[ind]):
                    globalReturn['MAonTop'].append(RangeMin)
                else:
                    globalReturn['MAonTop'].append(RangeMax)
                
    print(globalReturn)
    return globalReturn; 

SMAtoSMACompare(5,10)