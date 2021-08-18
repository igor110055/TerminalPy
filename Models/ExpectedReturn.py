import numpy as np
import pandas as pd
from pandas_datareader import data as wb
from datetime import date
today = date.today()

tickers = ['MSFT', 'TSLA']

data = pd.DataFrame()
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2012-1-1', end= today)['Adj Close']  
    
print(data)