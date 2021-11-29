from Simulator.PriceDiffenrence import PriceDiffPercent

def Formater2(HistoryObjFromRuntime2):
    x = HistoryObjFromRuntime2
    for index in range(len(HistoryObjFromRuntime2['Cash'])):
        if HistoryObjFromRuntime2['Cash'][0] == 0:
            pnl = PriceDiffPercent(HistoryObjFromRuntime2['Cash'])
            historyObj = {
                'Direction': 'Short',
                'Open': {
                    'Time': HistoryObjFromRuntime2['Time']
                },
                'Close': {
                    'Time': 'Position is still Open'
                }
            }
        elif HistoryObjFromRuntime2['AssetAmount'][0] == 0:
            pnl = PriceDiffPercent(HistoryObjFromRuntime2['AssetAmount'])
            # value = HistoryObjFromRuntime2['AssetAmount'][-1]*price
            historyObj = {
                'Direction': 'Long',
                'Open': {
                    'Time': HistoryObjFromRuntime2['Time'],
                },
                'Close': {
                    'Time': 'Position is still Open',
                }
            }
                
