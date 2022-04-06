import talib
import numpy

class Indicator:
    def __init__(self, price_data):
        self.price_raw = price_data
        self.price_data = None

        # set data to array on load
        self.data_to_array()

    def data_to_array(self):
        self.price_data = numpy.array(self.price_raw[1])

    def get_sma(self, data_range):
        sma = talib.SMA(self.price_data, data_range).tolist()
        return sma


"""
The rest of the talib items can be defined within this class as required - currently only the in-use items are added
"""
