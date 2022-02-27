IndicatorCategories = [
    'Overlap Studies',
    'Momentum Indicators',
    'Volume Indicators',
    'Volatility Indicators',
    'Price Transform',
    'Cycle Indicators',
    'Pattern Recognition',
    'Statistic Functions',
    'Math Transform',
    'Math Operators'
]

IndicatorsToRender = [  

        # {'Overlap Studies':[
        # ]},
            # {'name':'Bollinger Bands','symbol':'BBANDS'}, Output is an Array instead of Single Variable      
            {'name':'Double Exponential Moving Average','symbol':'DEMA'},        
            {'name':'Exponential Moving Average','symbol':'EMA'},        
            # {'name':'Hilbert Transform         Instantaneous Trendline','symbol':'HT_TRENDLINE'},
            {'name':'Kaufman Adaptive Moving Average','symbol':'KAMA'},        
            {'name':'Moving average','symbol':'MA'},        
            # {'name':'MESA Adaptive Moving Average','symbol':'MAMA'}, Output is an Array instead of Single Variable     
            # {'name':'Moving average with variable period','symbol':'MAVP'},        
            {'name':'MidPoint over period','symbol':'MIDPOINT'},        
            # {'name':'Midpoint Price over period','symbol':'MIDPRICE'},        
            # {'name':'Parabolic SAR','symbol':'SAR'},        
            # {'name':'Parabolic SAR         Extended','symbol':'SAREXT'},        
            {'name':'Simple Moving Average','symbol':'SMA'},
            {'name':'Triple Exponential Moving Average (T3)','symbol':'T3'},        
            {'name':'Triple Exponential Moving Average','symbol':'TEMA'},        
            {'name':'Triangular Moving Average','symbol':'TRIMA'},        
            {'name':'Weighted Moving Average','symbol':'WMA'},


        # {'Momentum Indicators':[
        # ]},
            {'name':'Average Directional Movement Index','symbol':'ADX'}, 
            {'name':'Average Directional Movement Index Rating','symbol':'ADXR'},
            # {'name':'Absolute Price Oscillator','symbol':'APO'},
            # {'name':'Aroon','symbol':'AROON'}, Output is an Array instead of Single Variable
            {'name':'Aroon Oscillator','symbol':'AROONOSC'},
            {'name':'Balance Of Power','symbol':'BOP'},
            {'name':'Commodity Channel Index','symbol':'CCI'},
            {'name':'Chande Momentum Oscillator','symbol':'CMO'},
            {'name':'Directional Movement Index','symbol':'DX'},
            # {'name':'Moving Average Convergence/Divergence','symbol':'MACD'},
            # {'name':'MACD with controllable MA type','symbol':'MACDEXT'},
            # {'name':'Moving Average Convergence/Divergence Fix 12/26','symbol':'MACDFIX'},
            # {'name':'Money Flow Index','symbol':'MFI'},
            {'name':'Minus Directional Indicator','symbol':'MINUS_DI'},
            {'name':'Minus Directional Movement','symbol':'MINUS_DM'},
            {'name':'Momentum','symbol':'MOM'},
            {'name':'Plus Directional Indicator','symbol':'PLUS_DI'},
            {'name':'Plus Directional Movement','symbol':'PLUS_DM'},
            {'name':'Percentage Price Oscillator','symbol':'PPO'},
            {'name':'Rate of change : ((price/prevPrice)-1)*1','symbol':'ROC'},
            {'name':'Rate of change Percentage: (price-prevPrice)/prevPrice','symbol':'ROCP'},
            {'name':'Rate of change ratio: (price/prevPrice)','symbol':'ROCR'},
            {'name':'Rate of change ratio 1'' scale: (price/prevPrice)*1','symbol':'ROCR1'''},
            {'name':'Relative Strength Index','symbol':'RSI'},
            # {'name':'Stochastic','symbol':'STOCH'},
            # {'name':'Stochastic Fast','symbol':'STOCHF'},
            # {'name':'Stochastic Relative Strength Index','symbol':'STOCHRSI'},
            {'name':'1-day Rate-Of-Change (ROC) of a Triple Smooth EMA','symbol':'TRIX'},
            # {'name':' Ultimate Oscillator','symbol':'ULTOSC'},
            {'name':'Williams R','symbol':'WILLR'},
        

        # {'Volume Indicators':[
        # ],
            {'name':'Chaikin A/D Line','symbol':'AD'},           
            {'name':'Chaikin A/D Oscillator','symbol':'ADOSC'},
            {'name':'On Balance Volume','symbol':'OBV'}, 


        # {'Volatility Indicators':[
        # ],       
            {'name':'Average True Range','symbol':'ATR'},
            {'name':'Normalized Average True Range','symbol':'NATR'},        
            {'name':'True Range','symbol':'TRANGE'},


        # {'Cycle Indicators':[
        # ],     
            {'name':'Hilbert Transform  Dominant Cycle Period ','symbol':'HT_DCPERIOD '},       
            {'name':'Hilbert Transform  Dominant Cycle Phase','symbol':'HT_DCPHASE  '},
            {'name':'Hilbert Transform  Phasor Component','symbol':'HT_PHASOR   '},         
            {'name':'Hilbert Transform  SineWave','symbol':'HT_SINE'},
            {'name':'Hilbert Transform  Trend vs Cycle Mode','symbol':'HT_TRENDMODE'},


        # {'Statistic Functions':[
        # ],      
            {'name':'Beta','symbol':'BETA'},
            {'name':'Pearsons Correlation Coefficient (r)','symbol':'CORREL'},
            {'name':'Linear Regression','symbol':'LINEARREG'},
            {'name':'Linear Regression Angle','symbol':'LINEARREG_ANGLE'},
            {'name':'Linear Regression Intercept','symbol':'LINEARREG_INTERCEPT'},
            {'name':'Linear Regression Slope','symbol':'LINEARREG_SLOPE'},
            {'name':'Standard Deviation','symbol':'STDDEV'},
            {'name':'Time Series Forecast','symbol':'TSF'},
            {'name':'Variance','symbol':'VAR'},


        # {'Math Transform':[
        # ],
            {'name':'Vector Trigonometric ACos ','symbol':'ACOS'},            
            {'name':'Vector Trigonometric ASin','symbol':'ASIN'},            
            {'name':'Vector Trigonometric ATan ','symbol':'ATAN'},            
            {'name':'Vector Ceil','symbol':'CEIL'},
            {'name':'Vector Trigonometric Cos','symbol':'COS'},           
            {'name':'Vector Trigonometric Cosh ','symbol':'COSH'},            
            {'name':'Vector Arithmetic Exp ','symbol':'EXP'},        
            {'name':'Vector Floor','symbol':'FLOOR'},            
            {'name':'Vector Log Natural','symbol':'LN'},     
            {'name':'Vector Log10','symbol':'LOG10'},
            {'name':'Vector Trigonometric Sin ','symbol':'SIN'},           
            {'name':'Vector Trigonometric Sinh','symbol':'SINH'},            
            {'name':'Vector Square Root','symbol':'SQRT'},     
            {'name':'Vector Trigonometric Tan ','symbol':'TAN'},           
            {'name':'Vector Trigonometric Tanh','symbol':'TANH'},        


        # {'Math Operators':[
        # ],
            {'name':'Vector Arithmetic Add ','symbol':'ADD'},        
            {'name':'Vector Arithmetic Div ','symbol':'DIV'},        
            {'name':'Highest value over a specified period','symbol':'MAX'},
            {'name':'Index of highest value over ','symbol':'MAXINDEX'}, 
            {'name':'Lowest value over a specified period','symbol':'MIN'},
            {'name':'Index of lowest value over a specified period','symbol':'MININDEX'},  
            {'name':'Lowest and highest values over a specified period','symbol':'MINMAX'},
            {'name':'Indexes of lowest and highest values over a specified period','symbol':'MINMAXINDEX '},
            {'name':'Vector Arithmetic Mult ','symbol':'MULT'},         
            {'name':'Vector Arithmetic Substraction','symbol':'SUB'}, 
            {'name':'Summation','symbol':'SUM'}


  ]
 
 