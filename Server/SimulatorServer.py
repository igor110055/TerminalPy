from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

def Server(Simulation):
    app = Flask(__name__)
    CORS(app)
    api = Api(app)

    @app.route('/Simulation')
    def Sim():
        return {'Simulation':Simulation}

    app.run(debug=True)