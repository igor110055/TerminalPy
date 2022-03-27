from crypt import methods
from Config.BinanceFetchFrontend import PriceDataFetch
import find_parent
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, request
from flask_cors import CORS
from copy import deepcopy

app = Flask(__name__)
CORS(app)
api = Api(app)

from Config.DataSourceFrontend import DataSources
@app.route('/DataSources', methods=['GET'])
def GetDataSources():
    return{'Metadata':DataSources()}
    

from Config.AssetPairsFrontend import AssetPairs
@app.route('/AssetPairs',methods = ['POST'])
def PostAssetPairs():
    data = request.get_json()
    selectedDataSource = data['DataSource']
    returnAssetPairs = AssetPairs(selectedDataSource)

    return {'AssetPairs': returnAssetPairs}

# Create Global Array in which all PriceData gets fetched
from PriceData.AveragePrices import getAveragePrice
GlobalPriceData = []

def AppendGlobalPriceData(toAppend):
    PriceData = deepcopy(getAveragePrice(toAppend))
    # print('Average in App.py', PriceData)
    GlobalPriceData.append({
        'config':toAppend['config'],
        'OHLC': toAppend['OHLC'],
        'Average': PriceData
    })

# Price Data ---------------------
from Config.OHLCDataFrontend import OHLCData
@app.route('/OHLC', methods=['POST'])
def OHLC():
    data = request.get_json()
    ohlcConfig = data['ohlcConfig']
    print(ohlcConfig)
    returnOHLCData = OHLCData(ohlcConfig)
    AppendGlobalPriceData({'config':ohlcConfig,'OHLC': returnOHLCData})
    return {'config':ohlcConfig,'OHLC': returnOHLCData}


# Indicators Data ---------------------
from Config.ListOfIndicatorsFrontend import IndicatorsToRender
@app.route('/ListAllIndicators', methods=['GET'])
def ListIndi():
    return {'IndicatorsToRender': IndicatorsToRender}


from Indicators.Rendered_Indicators import InitSelectedIndicator
from PriceData.BinanceOHLCforIndicators import OHLCformated
@app.route('/RenderIndicator', methods=['POST'])
def renderIndi():
    data = request.get_json()
    IndicatorConfig = data['config']
    if len(GlobalPriceData)>0:
        OHLCPrice = deepcopy(OHLCformated(GlobalPriceData[-1]['OHLC']))
        IndicatorReady = InitSelectedIndicator(
            IndicatorConfig['selectedIndicator']['symbol'], 
            OHLCPrice, 
            int(IndicatorConfig['selectedPeriod'])
        )
        return {
            'Indicator': IndicatorReady,
            'config': IndicatorConfig
        }

# Statistics Data ---------------------
from Models.AllModelsFrontend import AllModels 
@app.route('/AllModels', methods=['GET'])
def GetAllModels():
    return{'Metadata':AllModels()}

StatisticsPriceData = []

def AppendStatisticsPriceData(toAppend):
    PriceData = deepcopy(getAveragePrice(toAppend))
    # print('Average in App.py', PriceData)
    StatisticsPriceData.append({
        'config':toAppend['config'],
        'OHLC': toAppend['OHLC'],
        'Average': PriceData
    })

from Models.PriceData2DataFrame import Test , Creator
@app.route('/Statistics', methods=['POST'])
def Statistics():
    data = request.get_json()
    ohlcConfig = data['ohlcConfig']
    returnOHLCData = OHLCData(ohlcConfig)
    AppendStatisticsPriceData({'config':ohlcConfig,'OHLC': returnOHLCData})
    return {'StatisticsPriceData':StatisticsPriceData}




# Simulation Data ---------------------
from Config.ListOfStrategies import Strategies
@app.route('/ListAllStrategies', methods=['GET'])
def ListStrat():
    return {'Strategies': Strategies}

from SimulationApi import RunSimulation
# from PriceData.BinanceAveragePrice import AveragePrice
@app.route('/Simulation', methods=['POST'])
def Sim():
    if len(GlobalPriceData)>0:
        data = request.get_json()
        SimulationConfig = data['config']
        OHLCPrice = deepcopy(OHLCformated(GlobalPriceData[-1]['OHLC']))
        Simulation = RunSimulation(OHLCPrice,SimulationConfig)
        return {
            'Simulation': Simulation,
            'config': SimulationConfig
        }
      
    
# host='0.0.0.0'
app.run(host='localhost',port=5001,debug=True)