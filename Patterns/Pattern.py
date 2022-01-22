import requests
import pandas as pd
import numpy as np
import talib as talib

# link for Bitcoin Data
link = "https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD&limit=365&aggregate=1"

# API request historical
historical_get = requests.get(link)

# access the content of historical api request
historical_json = historical_get.json()

# extract json data as dictionary
historical_dict = historical_json['Data']

# extract Final historical df
df = pd.DataFrame(historical_dict,
                             columns=['close', 'high', 'low', 'open', 'time', 'volumefrom', 'volumeto'],
                             dtype='float64')

# time column is converted to "YYYY-mm-dd hh:mm:ss" ("%Y-%m-%d %H:%M:%S")
posix_time = pd.to_datetime(df['time'], unit='s')

# append posix_time
df.insert(0, "Date", posix_time)

# drop unix time stamp
df.drop("time", axis = 1, inplace = True)

# print(df)

# extract OHLC 
op = df['open']
hi = df['high']
lo = df['low']
cl = df['close']

candlePatterns = [
    'CDL2CROWS',
    'CDL3BLACKCROWS',
    'CDL3INSIDE',
    'CDL3LINESTRIKE',
    'CDL3OUTSIDE',
    'CDL3STARSINSOUTH',
    'CDL3WHITESOLDIERS',
    'CDLABANDONEDBABY',
    'CDLADVANCEBLOCK',
    'CDLBELTHOLD',
    'CDLBREAKAWAY',
    'CDLCLOSINGMARUBOZU',
    'CDLCONCEALBABYSWALL',
    'CDLCOUNTERATTACK',
    'CDLDARKCLOUDCOVER',
    'CDLDOJI',
    'CDLDOJISTAR',
    'CDLDRAGONFLYDOJI',
    'CDLENGULFING',
    'CDLEVENINGDOJISTAR',
    'CDLEVENINGSTAR',
    'CDLGAPSIDESIDEWHITE',
    'CDLGRAVESTONEDOJI',
    'CDLHAMMER',
    'CDLHANGINGMAN',
    'CDLHARAMI',
    'CDLHARAMICROSS',
    'CDLHIGHWAVE',
    'CDLHIKKAKE',
    'CDLHIKKAKEMOD',
    'CDLHOMINGPIGEON',
    'CDLIDENTICAL3CROWS',
    'CDLINNECK',
    'CDLINVERTEDHAMMER',
    'CDLKICKING',
    'CDLKICKINGBYLENGTH',
    'CDLLADDERBOTTOM',
    'CDLLONGLEGGEDDOJI',
    'CDLLONGLINE',
    'CDLMARUBOZU',
    'CDLMATCHINGLOW',
    'CDLMATHOLD',
    'CDLMORNINGDOJISTAR',
    'CDLMORNINGSTAR',
    'CDLONNECK',
    'CDLPIERCING',
    'CDLRICKSHAWMAN',
    'CDLRISEFALL3METHODS',
    'CDLSEPARATINGLINES',
    'CDLSHOOTINGSTAR',
    'CDLSHORTLINE',
    'CDLSPINNINGTOP',
    'CDLSTALLEDPATTERN',
    'CDLSTICKSANDWICH',
    'CDLTAKURI',
    'CDLTASUKIGAP',
    'CDLTHRUSTING',
    'CDLTRISTAR',
    'CDLUNIQUE3RIVER',
    'CDLUPSIDEGAP2CROWS',
    'CDLXSIDEGAP3METHODS',
    
]

# pattern  = requests.get('pattern', False)
# pattern_function = getattr(talib, pattern)
# allPatterns = getattr(talib)
# print(allPatterns)


# numm = talib.CDL2CROWS(op,hi,lo,cl)
# print(numm[numm != 0])




# for i in candlePatterns:
#     f = getattr(talib, i)
#     result = f(op,hi,lo,cl)
#     print(i)
#     print(result[result != 0])
    




# df['candlestick_pattern'] = np.nan
# df['candlestick_match_count'] = np.nan
# for index, row in df.iterrows():

#     # no pattern found
#     if len(row[candle_names]) - sum(row[candle_names] == 0) == 0:
#         df.loc[index,'candlestick_pattern'] = "NO_PATTERN"
#         df.loc[index, 'candlestick_match_count'] = 0
#     # single pattern found
#     elif len(row[candle_names]) - sum(row[candle_names] == 0) == 1:
#         # bull pattern 100 or 200
#         if any(row[candle_names].values > 0):
#             pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bull'
#             df.loc[index, 'candlestick_pattern'] = pattern
#             df.loc[index, 'candlestick_match_count'] = 1
#         # bear pattern -100 or -200
#         else:
#             pattern = list(compress(row[candle_names].keys(), row[candle_names].values != 0))[0] + '_Bear'
#             df.loc[index, 'candlestick_pattern'] = pattern
#             df.loc[index, 'candlestick_match_count'] = 1
#     # multiple patterns matched -- select best performance
#     else:
#         # filter out pattern names from bool list of values
#         patterns = list(compress(row[candle_names].keys(), row[candle_names].values != 0))
#         container = []
#         for pattern in patterns:
#             if row[pattern] > 0:
#                 container.append(pattern + '_Bull')
#             else:
#                 container.append(pattern + '_Bear')
#         rank_list = [candle_rankings[p] for p in container]
#         if len(rank_list) == len(container):
#             rank_index_best = rank_list.index(min(rank_list))
#             df.loc[index, 'candlestick_pattern'] = container[rank_index_best]
#             df.loc[index, 'candlestick_match_count'] = len(container)
#     # clean up candle columns
#     df.drop(candle_names, axis = 1, inplace = True)

# CDL2CROWS            Two Crows
# CDL3BLACKCROWS       Three Black Crows
# CDL3INSIDE           Three Inside Up/Down
# CDL3LINESTRIKE       Three-Line Strike
# CDL3OUTSIDE          Three Outside Up/Down
# CDL3STARSINSOUTH     Three Stars In The South
# CDL3WHITESOLDIERS    Three Advancing White Soldiers
# CDLABANDONEDBABY     Abandoned Baby
# CDLADVANCEBLOCK      Advance Block
# CDLBELTHOLD          Belt-hold
# CDLBREAKAWAY         Breakaway
# CDLCLOSINGMARUBOZU   Closing Marubozu
# CDLCONCEALBABYSWALL  Concealing Baby Swallow
# CDLCOUNTERATTACK     Counterattack
# CDLDARKCLOUDCOVER    Dark Cloud Cover
# CDLDOJI              Doji
# CDLDOJISTAR          Doji Star
# CDLDRAGONFLYDOJI     Dragonfly Doji
# CDLENGULFING         Engulfing Pattern
# CDLEVENINGDOJISTAR   Evening Doji Star
# CDLEVENINGSTAR       Evening Star
# CDLGAPSIDESIDEWHITE  Up/Down-gap side-by-side white lines
# CDLGRAVESTONEDOJI    Gravestone Doji
# CDLHAMMER            Hammer
# CDLHANGINGMAN        Hanging Man
# CDLHARAMI            Harami Pattern
# CDLHARAMICROSS       Harami Cross Pattern
# CDLHIGHWAVE          High-Wave Candle
# CDLHIKKAKE           Hikkake Pattern
# CDLHIKKAKEMOD        Modified Hikkake Pattern
# CDLHOMINGPIGEON      Homing Pigeon
# CDLIDENTICAL3CROWS   Identical Three Crows
# CDLINNECK            In-Neck Pattern
# CDLINVERTEDHAMMER    Inverted Hammer
# CDLKICKING           Kicking
# CDLKICKINGBYLENGTH   Kicking - bull/bear determined by the longer marubozu
# CDLLADDERBOTTOM      Ladder Bottom
# CDLLONGLEGGEDDOJI    Long Legged Doji
# CDLLONGLINE          Long Line Candle
# CDLMARUBOZU          Marubozu
# CDLMATCHINGLOW       Matching Low
# CDLMATHOLD           Mat Hold
# CDLMORNINGDOJISTAR   Morning Doji Star
# CDLMORNINGSTAR       Morning Star
# CDLONNECK            On-Neck Pattern
# CDLPIERCING          Piercing Pattern
# CDLRICKSHAWMAN       Rickshaw Man
# CDLRISEFALL3METHODS  Rising/Falling Three Methods
# CDLSEPARATINGLINES   Separating Lines
# CDLSHOOTINGSTAR      Shooting Star
# CDLSHORTLINE         Short Line Candle
# CDLSPINNINGTOP       Spinning Top
# CDLSTALLEDPATTERN    Stalled Pattern
# CDLSTICKSANDWICH     Stick Sandwich
# CDLTAKURI            Takuri (Dragonfly Doji with very long lower shadow)
# CDLTASUKIGAP         Tasuki Gap
# CDLTHRUSTING         Thrusting Pattern
# CDLTRISTAR           Tristar Pattern
# CDLUNIQUE3RIVER      Unique 3 River
# CDLUPSIDEGAP2CROWS   Upside Gap Two Crows
# CDLXSIDEGAP3METHODS  Upside/Downside Gap Three Methods
