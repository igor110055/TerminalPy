import copy
def Formater(OutputRuntimeSimulator):
    CopiedOutputRuntimeSimulator = copy.deepcopy(OutputRuntimeSimulator)
    for element in CopiedOutputRuntimeSimulator['Trades']:
        index = CopiedOutputRuntimeSimulator['Trades'].index(element)
        if index > 0:
            element['Open']['Collateral'] = CopiedOutputRuntimeSimulator['Trades'][index - 1]['Close']['Collateral']
        
        if index < 4:
            element['Close']['Time'] = CopiedOutputRuntimeSimulator['Trades'][index + 1]['Open']['Time']
    
    return CopiedOutputRuntimeSimulator