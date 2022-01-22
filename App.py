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
    print('returnAssetPairs',returnAssetPairs)
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
    returnOHLCData = OHLCData(ohlcConfig)
    AppendGlobalPriceData({'config':ohlcConfig,'OHLC': returnOHLCData})
    return {'config':ohlcConfig,'OHLC': returnOHLCData}


# Indicators Data ---------------------
from Config.ListOfIndicatorsFrontend import IndicatorsToRender
@app.route('/ListAllIndicators', methods=['GET'])
def ListIndi():
    return {'IndicatorsToRender': IndicatorsToRender}

from VisualiserApi import IndicatorGenerator
@app.route('/Indicators', methods=['GET'])
def Indi():
    if len(GlobalPriceData)>0:
        PriceData = deepcopy(GlobalPriceData[-1]['Average'])
        Indicators = IndicatorGenerator(PriceData)
        return {'Indicators': Indicators}
        
    return {'Test': 'len(GlobalPriceData)>0: = false'}

# Simulation Data ---------------------
from Config.ListOfStrategies import Strategies
@app.route('/ListAllStrategies', methods=['GET'])
def ListStrat():
    return {'Strategies': Strategies}

from SimulationApi import RunSimulation
@app.route('/Simulation')
def Sim():
    if len(GlobalPriceData)>0:
        PriceData = deepcopy(GlobalPriceData[-1]['Average'])
        Simulation = RunSimulation(PriceData)
        return {
            'Simulation': Simulation,
        }
    

app.run(host='localhost',port=5001,debug=True)