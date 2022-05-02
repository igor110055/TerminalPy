import find_parent
import talib

from PriceData.BinanceFetch import PriceDataFetch
from Models.PriceData2DataFrame import BinanceDataFrame

class AllCandlePatterns():
    def __init__(self, price_data, data_frame_template):
        self.price_data = price_data()
        self.frame = data_frame_template(self.price_data)
        

    def screening(self):
        positives = []
        available_patterns = talib.get_function_groups()['Pattern Recognition']

        test_frame = self.frame
        test_frame.ohlc()

        for element in available_patterns:
            method_to_call = getattr(talib, element)
            frame = method_to_call(
                    test_frame.PriceDataFrame['Open'],
                    test_frame.PriceDataFrame['High'],
                    test_frame.PriceDataFrame['Low'],
                    test_frame.PriceDataFrame['Close'],
            )
            non_0_frame = frame[frame != 0]
            non_0_list = non_0_frame.values.tolist()
            
            if len(non_0_list) > 0:
                dates_list = list(non_0_frame.index.values)
                # Covert all dates in the list to integer
                for date in dates_list:
                    index = dates_list.index(date)
                    dates_list[index] = int(date)
                
                positives.append({'Pattern': element, 'Time': dates_list, 'Value': non_0_list})
            
        return positives


# test_run = AllCandlePatterns(PriceDataFetch, BinanceDataFrame)
# lol = test_run.screening()
