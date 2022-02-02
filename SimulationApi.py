import find_parent
from Simulator.SelectIndicator import InitSelectedIndicator
import Indicators.Indicator as Indicator
from Strategies.MACrossings import SMAtoSMACompare as Line2LineCompare
from Simulator.Runtime import Simulator
from Simulator.RuntimeOutputFormater import Formater

def RunSimulation(PriceData,Config):
    
    Indicator1 = InitSelectedIndicator(
        Config['Indicator1']['symbol'],
        PriceData,
        int(Config['Period1'])
    )
    
    Indicator2 = InitSelectedIndicator(
        Config['Indicator2']['symbol'],
        PriceData,
        int(Config['Period2']) 
    )

    LineCrossings = Line2LineCompare(Indicator1 , Indicator2)
    
    Simulation = Simulator(LineCrossings)

    Formater2Test = Formater(Simulation)

    return Formater2Test
