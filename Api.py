from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import ast

def Server(CandleSticks, Indicators):
    app = Flask(__name__)
    CORS(app)
    api = Api(app)


    @app.route('/Indicators')
    def index():
        return {'Indicators':Indicators}

    @app.route('/OHLC')
    def OHLC():
        return {'OHLC':CandleSticks}

    app.run(debug=True)