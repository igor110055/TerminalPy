import OHLC_data_CCXT
import talib as talib
import numpy
from datetime import datetime
 
# #creating empty lists
# op = []
# hi = []
# lo = []
# cl = [] 

# #pushing data into lists
# for element in OHLC_data_CCXT.ohlc:
#     op.append(element[1])
#     hi.append(element[2])
#     lo.append(element[3])
#     cl.append(element[4])

# # converting list to array (for talib)
# open = numpy.array(op)
# high = numpy.array(hi)
# low = numpy.array(lo)
# close = numpy.array(cl)


# Average = [[],[]]

# #Pushing Data into the Average List
# for element in OHLC_data_CCXT.ohlc:
#     readable = datetime.fromtimestamp(element[0]/1000).isoformat()    
#     Average[0].append(str(readable))
    

# #Calculating Average Price
# for element in talib.AVGPRICE(open,high,low,close).tolist():
#     Average[1].append(element)


def AveragePrice(CandleData):
    #creating empty lists
    op = []
    hi = []
    lo = []
    cl = [] 

    #pushing data into lists
    for element in CandleData:
        op.append(element[1])
        hi.append(element[2])
        lo.append(element[3])
        cl.append(element[4])

    # converting list to array (for talib)
    open = numpy.array(op)
    high = numpy.array(hi)
    low = numpy.array(lo)
    close = numpy.array(cl)


    Average = [[],[]]

    #Pushing Data into the Average List
    for element in CandleData:
        readable = datetime.fromtimestamp(element[0]/1000).isoformat()    
        Average[0].append(str(readable))
        

    #Calculating Average Price
    for element in talib.AVGPRICE(open,high,low,close).tolist():
        Average[1].append(element)

    return Average
    

# AveragePrice(OHLC_data_CCXT.ohlc)