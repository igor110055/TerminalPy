import OHLC_data
import talib as talib
import numpy
 
#creating empty lists
op = []
hi = []
lo = []
cl = [] 

Average = [[],[]]

#pushing data into lists
for element in OHLC_data.ohlc:
    Average[0].append(element[0])
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
for element in talib.AVGPRICE(open,high,low,close).tolist():
    Average[1].append(element)
    

# print(Average)