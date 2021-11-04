import sys
sys.path.insert(1,'/home/hackerboi/Dokumente/python/TerminalPy/Indicators')

def SortMAX_MIN(List_of_Indicators):
    #Compare two MA Ranges and filtering the min and max value
    Range_min = min(List_of_Indicators[0]['range'], List_of_Indicators[1]['range'])
    Range_max = max(List_of_Indicators[0]['range'], List_of_Indicators[1]['range'])
    MaxValue = []
    MinValue = []

    for element in List_of_Indicators:
        if element['range'] == Range_max:
            MaxValue.append(element)
        elif element['range'] == Range_min:
            MinValue.append(element)

    return {
        'RangeMax': Range_max,
        'RangeMin': Range_min,
        'MaxValue': MaxValue[0]['value'],
        'MinValue': MinValue[0]['value'],
        'Time': MaxValue[0]['time'],
        'AssetValue':MaxValue[0]['assetValue']
    }