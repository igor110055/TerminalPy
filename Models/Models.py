"""Module"""

# from scipy import stats
# import statsmodels.api as sm
import numpy as np
from Models.PriceData2DataFrame import Creator

class Modelz():
    """Class"""
    def __init__(self,StatisticsPriceData) -> None:
        self.data_frame_instance = Creator(StatisticsPriceData)
        self.Dataframe = self.data_frame_instance.PriceData

    def rates_of_logarithmic_volatility(self):
        """Method"""
        for rowName, rowData in self.Dataframe.iteritems():
            self.Dataframe[rowName] = np.log(self.Dataframe[rowName] / self.Dataframe[rowName].shift(1))
        print(self.Dataframe.values.tolist())
        return self.Dataframe.values.tolist()

    def rates_of_simple_volatility(self):
        """Method"""
        for rowName, rowData in self.Dataframe.iteritems():
            self.Dataframe[rowName] = (self.Dataframe[rowName] / self.Dataframe[rowName].shift(1)) - 1
        print(self.Dataframe.values.tolist())
        return self.Dataframe.values.tolist()

        # for rowName, rowData in self.Dataframe.iteritems():
        #     self.Dataframe['Simple Return'] = (self.Dataframe[rowName] / self.Dataframe[rowName].shift(1)) - 1
        #     self.Dataframe['Logarithmic Return'] = np.log(self.Dataframe[rowName] / self.Dataframe[rowName].shift(1))
        #     self.Jochen = self.Dataframe.values.tolist()
        #     self.dictToReturn.append(self.Jochen)
        #     print('Jochen', self.Jochen)
            # print(rowName+' Simple Return raw: ',self.Dataframe['Simple Return'])
            # print(rowName+' Logarithmic Return raw: ',self.Dataframe['Logarithmic Return'])


    def rates_of_return(self):
        """Method"""
        normalized_list = (self.Dataframe / self.Dataframe.iloc[0] * 100)
        print(normalized_list.values.tolist())
        return normalized_list.values.tolist()


    def rates_of_deviation(self):
        """Method"""
        for rowName, rowData in self.Dataframe.iteritems():
            print(rowName)
            print(np.log(self.Dataframe[rowName] / self.Dataframe[rowName].shift(1)))

    # def Rates_of_Corelation(self):
    #     pass
