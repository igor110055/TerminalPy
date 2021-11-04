import sys
sys.path.insert(0, '/home/hackerboi/Dokumente/python/TerminalPy/Indicators')

from MAFormater import IndicatorsToFormate

def SMAtoSMACompare(Indicat0r1raw, Indicator2raw):
    #Formating the Indicators Correctly
    Indicat0r1 = IndicatorsToFormate(Indicat0r1raw)
    Indicator2 = IndicatorsToFormate(Indicator2raw)
    
    # Sort Indicators from Min to Max
    

    #Compare two MA Ranges and filtering the min and max value
    RangeMin = min(Indicat0r1['range'], Indicator2['range'])
    RangeMax = max(Indicat0r1['range'], Indicator2['range'])

    MaxRangeValue = []
    MinRangeValue = []
    # #Dummy Data Set
    # RangeValueMin = [1,2,3,4,5,10,10,10,10,10,10,10,10,10,10,10,10]
    # RangeValueMax =           [10,15,20,9,9,9,11,11,11,9,8,7]

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
                globalReturn['time'].append(RangeValueMin[index + difference])
                globalReturn['AssetValue'].append(round(RangeValueMin[index + difference]))
                
                globalReturn['MAMin']['value'].append(round(RangeValueMin[index + difference]))
                globalReturn['MAMax']['value'].append(round(RangeValueMax[index]))
                
                #Log wich MA element is on top of the other
                if (RangeValueMin[index + difference] > RangeValueMax[index]):
                    globalReturn['MAonTop'].append(RangeMin)
                else:
                    globalReturn['MAonTop'].append(RangeMax)
                
    return globalReturn; 
