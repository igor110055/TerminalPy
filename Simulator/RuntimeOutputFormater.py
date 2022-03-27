# Takes the Cash/Asset Ballance from every Position and Calculates the PnL relative to the 
# Position before it

def Formater(HistoryObjFromRuntime2):
    for index in range(1, len(HistoryObjFromRuntime2['Trades'])):
        element1 = HistoryObjFromRuntime2['Trades'][index - 1]['From']     
        element2 = HistoryObjFromRuntime2['Trades'][index]['To']  
        if element1 == 0:
            continue
        changePercentage = ((element2 / element1) - 1) * 100
        # Adding a PnL key/value pair to each trade
        HistoryObjFromRuntime2['Trades'][index]['PnL'] =  round(changePercentage, 2)      

    return HistoryObjFromRuntime2
