import talib
import numpy
from math import sqrt
import random


class DummyStrategy:
    def __init__(self, price_data):
        self.price_raw = price_data
        self.price_data = None

        # set data to array on load
        # self.data_to_array()

    # def data_to_array(self):
    #     self.price_data = numpy.array(self.price_raw[1])

    def execute(self):
        globalReturn = {
        'Time': [],
        'AssetValue': [],
        'Action': []
        }

        for element in self.price_raw[1]:
            index_ = self.price_raw[1].index(element)
            prime_flag = 0
            
            if(index_ > 1):
                for i in range(2, int(sqrt(index_)) + 1):
                    if (index_ % i == 0):
                        prime_flag = 1
                        break
                if (prime_flag == 0):
                    # print("PrimeNumber: ", index_, 'buy')
                    globalReturn['Action'].append({'type':'buy','positionSize': 0.5})
                    globalReturn['AssetValue'].append(self.price_raw[1][index_])
                    globalReturn['Time'].append(self.price_raw[0][index_])
                elif(index_ % 2 == 0):
                    # print("StraightNumber: ", index_, 'sell')
                    globalReturn['Action'].append({'type':'sell','positionSize': 0.5})
                    globalReturn['AssetValue'].append(self.price_raw[1][index_])
                    globalReturn['Time'].append(self.price_raw[0][index_])
            
        print(globalReturn)
        return globalReturn


class DummyStrategy2:
    def __init__(self, price_data):
        self.price_raw = price_data
        self.price_data = None

        # set data to array on load
        # self.data_to_array()

    # def data_to_array(self):
    #     self.price_data = numpy.array(self.price_raw[1])

    def execute(self):
        globalReturn = {
        'Time': [],
        'AssetValue': [],
        'Action': []
        }

        for element in self.price_raw[1]:
            index_ = self.price_raw[1].index(element)
            
            n = random.random()
            if (n >= 0.75):
                print("RandomNumber >= 0.75: ", n, 'buy')
                globalReturn['Action'].append({'type':'buy','positionSize': 0.5})
                globalReturn['AssetValue'].append(self.price_raw[1][index_])
                globalReturn['Time'].append(self.price_raw[0][index_])
            elif(n <= 0.25):
                print("RandomNumber <= 0.25: ", n, 'sell')
                globalReturn['Action'].append({'type':'sell','positionSize': 0.5})
                globalReturn['AssetValue'].append(self.price_raw[1][index_])
                globalReturn['Time'].append(self.price_raw[0][index_])
        
        print(globalReturn)
        return globalReturn