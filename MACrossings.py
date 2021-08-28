from math import log
import Indicator
from getRidofNan import delNan



def SMAtoSMACompare(MARange1, MARange2):
    #Compare two MA Ranges and filtering the min and max value
    RangeMin = min(MARange1, MARange2)
    RangeMax = max(MARange1, MARange2)

    #Dummy Data Set
    RangeValueMin = [1,2,3,4,5,10,20,10,10,50]
    RangeValueMax = [100,10,20,30,40]

    #Get historical MA Values 
    #and deleting all nan values from the data list
    # RangeValueMin = delNan(Indicator.SMA(RangeMin))
    # RangeValueMax = delNan(Indicator.SMA(RangeMax))

    #The Dict we return
    globalReturn = {
        'time': [],
        'value': [],
        'MAMin': {
            'Range': RangeMin,
            'value': []
        },
        'MAMax': {
            'Range': RangeMax,
            'value': []
        },
        'MAonTop': [],

    }
    changeWatcher = []
    #Get the difference between min and max
    difference = (max(MARange1, MARange2)-min(MARange1, MARange2))

    for element in RangeValueMax:
        ind = RangeValueMax.index(element)
        #---Just for debugging
        mini = RangeValueMin[ind + difference]
        maxi = RangeValueMax[ind]
        #---
        comp = RangeValueMin[ind + difference]>RangeValueMax[ind]
        changeWatcher.append(comp)
        
        
        #Make sure Changewatcher only has two entries a time
        if (len(changeWatcher) > 2):
            #Look out if the first or last element gets entfernt, Logic error
            # changeWatcher.pop(len(changeWatcher)-1)
            changeWatcher = changeWatcher[:-1]
            print(changeWatcher, element)
            #Weil ChangeWatcher immer [True, True], wird das nächste if statement nich getriggert
            
            #Codeblock never executes!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            #Listens to wether a MA Crossing occours
            if (changeWatcher[0] != changeWatcher[1]):
                # print(changeWatcher)
                #Data needs to be supplied from Indicator function
                #globalReturn['time'].append(RangeValueMax.time[element])
                #globalReturn['value'].append((RangeValueMin.value[element + difference] + RangeValueMax[element])/2)
                
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