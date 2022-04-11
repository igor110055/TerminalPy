import find_parent
import talib

from PriceData.BinanceFetch import PriceDataFetch
from Models.PriceData2DataFrame import BinanceDataFrame

test_data = PriceDataFetch()
test_frame = BinanceDataFrame(test_data)
test_frame.ohlc()


def all_candle_patterns(price_data):
    positives = []
    available_patterns = talib.get_function_groups()['Pattern Recognition']

    test_frame = BinanceDataFrame(price_data)
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
            index_list = list(non_0_frame.index.values)
            positives.append({'Pattern': element, 'Time': index_list, 'Value': non_0_list})
        
    return positives


