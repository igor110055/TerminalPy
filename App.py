import find_parent
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, request
from flask_cors import CORS

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

GlobalOHLC = []

def GlobalAvergePrice(toAppend):
    GlobalOHLC.append(toAppend)
    
from Config.OHLCDataFrontend import OHLCData
@app.route('/OHLC', methods=['POST'])
def OHLC():
    data = request.get_json()
    ohlcConfig = data['ohlcConfig']
    returnOHLCData = OHLCData(ohlcConfig)
    GlobalAvergePrice({'config':ohlcConfig,'OHLC': returnOHLCData})
    return {'config':ohlcConfig,'OHLC': returnOHLCData}

from PriceData.AverageWDate import AveragePrice
from VisualiserApi import IndicatorGenerator
@app.route('/Indicators', methods=['GET'])
def Indi():
    if len(GlobalOHLC)>0:
        print('GlobalOHLC',GlobalOHLC[-1])
        PriceData = AveragePrice(GlobalOHLC[-1]['OHLC'])
        print(PriceData)
        Indicators = IndicatorGenerator(PriceData)
        return {'Indicators': Indicators}


from SimulationApi import RunSimulation
@app.route('/Simulation')
def Sim():
    if len(GlobalOHLC)>0:
        PriceData = AveragePrice(GlobalOHLC[-1]['OHLC'])
        print(PriceData)
        Simulation = RunSimulation(PriceData)
        print(Simulation)
        return {'Simulation': Simulation}
    
    return {'Test': 'len(GlobalOHLC)>0: = false'}

app.run(host='localhost',port=5001,debug=True)