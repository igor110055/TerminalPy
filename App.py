#Import Dependencies
import numpy
from Api import Server

#Import Price Data
from AveragePrice import Average
from OHLC_data import ohlc

#Import Indicators (TA-Lib)
import Indicator

#Import Strategies

#Initalize Indicators and convert it to a list
RSI30 = Indicator.RSI(30)


#Put all indicators into a dict 
Indicators = {
    'RSI30': RSI30 
}

# Server(ohlc, Indicators)

