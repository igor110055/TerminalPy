import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Indicators')

#from math import log
import Indicator
from getRidofNan import delNan

def SMAtoSMACompare(MARange1, MARange2, PriceData):
    #Compare two MA Ranges and filtering the min and max value
    RangeMin = min(MARange1, MARange2)
    RangeMax = max(MARange1, MARange2)

    # Get the Difference between two MA Ranges to match the output offset
    difference = RangeMax-RangeMin

    # #Dummy Data Set
    # RangeValueMin = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    # RangeValueMax =           [9,15,20,9,9,9,11,11,11,9,9,9]

    #Get historical MA Values and Delete all NAN Values
    RangeValueMinWnan = Indicator.SMA(PriceData,RangeMin)
    RangeValueMaxWnan = Indicator.SMA(PriceData,RangeMax)

    #and deleting all nan values from the data list
    RangeValueMin = [delNan(RangeValueMinWnan[0]),[]]
    RangeValueMax = [delNan(RangeValueMaxWnan[0]),[]]
    
    for element in range(RangeMin,len(PriceData[0])):
        RangeValueMin[1].append(PriceData[0][element])
        
    for element in range(RangeMax,len(PriceData[0])):
        RangeValueMax[1].append(PriceData[0][element])
        

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

    for element in RangeValueMax[0]:
        # Get the Index Number of each Element
        index = RangeValueMax[0].index(element)
        
        #Compare all values to each other
        comp = RangeValueMin[0][index + difference] > RangeValueMax[0][index]
        changeWatcher.append(comp)

        #Make sure Changewatcher only has two entries a time
        if (len(changeWatcher) > 2):
            
            #Take away the first(left side) element 
            changeWatcher = changeWatcher[1:]
            #Listens to wether a MA Crossing occours
            if (changeWatcher[0] != changeWatcher[1]):
                #Data needs to be supplied from Indicator function
                # globalReturn['time'].append(RangeValueMax[1][index])
                # globalReturn['AssetValue'].append(round(PriceData[1][index + RangeMax]))
                
                globalReturn['MAMin']['value'].append(round(RangeValueMin[0][index + difference]))
                globalReturn['MAMax']['value'].append(round(RangeValueMax[0][index]))
                
                #Log wich MA element is on top of the other
                if (RangeValueMin[0][index + difference] > RangeValueMax[0][index]):
                    globalReturn['MAonTop'].append(RangeMin)
                else:
                    globalReturn['MAonTop'].append(RangeMax)
                
    return globalReturn; 
