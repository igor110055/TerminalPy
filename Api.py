from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import ast

# import lol.py
import AveragePrice
from OHLC_data import ohlc

#formating OHLC
print(type(ohlc))

lol = ['RR', 'S']

app = Flask(__name__)
CORS(app)
api = Api(app)
@app.route('/Indicators')
def index():
    return {'OHLC': ohlc}

@app.route('/OHLC')
def OHLC():
    return lol

app.run(debug=True)