def ModelData(config, DataFrame):
    print(config['Selected_Model'])
    if config['Selected_Model'] == 'Rates of Simple Volatility':
        return DataFrame.Rates_of_Simple_Volatility()
    elif config['Selected_Model'] == 'Rates of Logarithmic Volatility':
        return DataFrame.Rates_of_Logarithmic_Volatility()
    elif config['Selected_Model'] == 'Rates of Return':
        return DataFrame.Rates_of_Return()
    elif config['Selected_Model'] == 'Rates of Deviation':
        return DataFrame.Rates_of_Deviation()
    elif config['Selected_Model'] == 'Rates of Deviation':
        return
   