import OHLC_data_CCXT
import talib as talib
import numpy
 
#creating empty lists
op = []
hi = []
lo = []
cl = [] 

#pushing data into lists
for element in OHLC_data_CCXT.ohlc:
    op.append(element[1])
    hi.append(element[1])
    lo.append(element[1])
    cl.append(element[1])

# converting list to array (for talib)
open = numpy.array(op)
high = numpy.array(hi)
low = numpy.array(lo)
close = numpy.array(cl)

#Calculating Average Price
Average = talib.AVGPRICE(open,high,low,close)

#print(Average)

