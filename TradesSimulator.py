#Import Strategy
import MACrossings
import Indicator
from AppendDatePrice import AppendDatePrice

#Apending Date and Price to an Indicator Output
SMA30 = Indicator.SMA(30)
Testen = AppendDatePrice(SMA30)

#Pair ETHUSD
#BaseCollateral example:USD
BaseCollateral = 130

#Specify when Sold or bought
# for element in Testen:
    
