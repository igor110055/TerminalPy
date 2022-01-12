from flask import Flask, request
from flask_restful import Resource, Api, reqparse, request
from flask_cors import CORS
# from requests.api import request

def Server(DataSources,CandleSticks, Indicators):
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    @app.route('/DataFetcher')
    def DataFetch():
        return{'Metadata':DataSources}
        # if request.method == 'POST':
        #     user = request.form['nm']
        #     print(user)

    @app.route('/Indicators', methods=['GET'])
    def Indi():
        return {'Indicators':Indicators}

    @app.route('/OHLC', methods=['GET'])
    def OHLC():
        return {'OHLC':CandleSticks}

    @app.route('/Posten',methods = ['POST'])
    def Postn():
        data = request.get_json()
        test = data['Test']
        print(test)
        return 'Moin'

    app.run(host='localhost',port=5001,debug=True)