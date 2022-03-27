"""
This is the object oriented version of the "Price data" folder
One benefit of using these class calls can be seen in app.py wherein the binUrl can be inserted later on
This allows for any data source to be used at runtime.
"""
import requests
import numpy
from datetime import datetime
import talib


class ImportData:
    def __init__(self):
        self.binUrl = 'https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=70'
        self.formatted = []
        self.json = None
        self.connect_data()
        self.is_formatted = False

    def connect_data(self, url=None):
        if url is not None:
            self.binUrl = url
        response = requests.get(self.binUrl)
        self.json = response.json()
        # new data has been loaded, thus not formatted
        self.is_formatted = False

    def format_data(self):
        """
        It can be advantageous to determine whether data has been formatted already
        This has the benefit of code readability wherein "format_data" is always called, but the system doesn't have to
        re-run the format if not required
        """
        if self.is_formatted:
            return True

        for element in self.json:
            op = round(float(element[1]), 3)
            hi = round(float(element[2]), 3)
            lo = round(float(element[3]), 3)
            cl = round(float(element[4]), 3)
            self.formatted.append([element[0], op, hi, lo, cl])
        self.is_formatted = True
        return True

    def get_format_data(self):
        if len(self.formatted) < 1:
            self.format_data()
        return self.formatted

    def reset_format_data(self):
        self.formatted = []


class AveragePrice:
    def __init__(self, candle_data):
        self.data = candle_data
        self.average = [[], []]

    def calc_average(self):
        op = []
        hi = []
        lo = []
        cl = []
        for data in self.data:
            self.average[0].append(f"{datetime.fromtimestamp(data[0] / 1000).isoformat}")
            op.append(data[1])
            hi.append(data[2])
            lo.append(data[3])
            cl.append(data[4])
        op = numpy.array(op)
        hi = numpy.array(hi)
        lo = numpy.array(lo)
        cl = numpy.array(cl)

        # for time in self.data:
        #     self.average[0].append(f"{datetime.fromtimestamp(time[0]/1000).isoformat}")

        for averaged_price in talib.AVGPRICE(op, hi, lo, cl).tolist():
            self.average[1].append(averaged_price)

    def get_average(self):
        if len(self.average[0]) == 0 or len(self.average[1]) == 0:
            self.calc_average()
        return self.average
