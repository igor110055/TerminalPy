#Config
#  config reformatted in OO_Overhaul
# from Config.Config import PriceData
# import Indicators.Indicator as Indicator
from Strategies.MACrossings import SMAtoSMACompare
from Strategies.DummyStrategy.DummyStrategyOOP import DummyStrategy, DummyStrategy2
from Simulator.Runtime import Simulator
from Simulator.RuntimeOutputFormater import Formater
from OO_Overhaul.data_handling import ImportData, AveragePrice
from OO_Overhaul.indicator import Indicator

from Simulator.RuntimeOOP import SimulatorOOP
# Load datasource
data_source = ImportData()
# bitcoin data auto loaded on init, to connect a different url call:
# data_source.connect_data(url="[optional alternate data url]")
if not data_source.format_data():
    print("Error in data format!")
    exit(1)
data_averaging = AveragePrice(data_source.get_format_data())
price_data = data_averaging.get_average()


# Declaring 2 Indicators with our Bitcoin PriceData
indicated_prices = Indicator(price_data)
SMA5 = indicated_prices.get_sma(5)
SMA10 = indicated_prices.get_sma(10)


# This is a module which compares 2 Moving Averages to each other
# with this output the Simulator module will be able to detect 
# when the Moving Average lines cross each other

# more_odered_output_strategy = DummyStrategy(price_data)
# more_odered_output_strategy.execute()

random_output_strategy = DummyStrategy2(price_data)
test2 = random_output_strategy.execute()

simulation_instance = SimulatorOOP(test2)
simulation_instance.execute()
history = simulation_instance.return_history()



# SMA5vs10 = SMAtoSMACompare(SMA10, SMA5)


# Simulation = Simulator(SMA5vs10)
# The Output from the Simulater Module needs to be analyzed to 
# tell us if we would have gained or losst money executing that Strategy
FormatedSimulation = Formater(history)

print(FormatedSimulation)