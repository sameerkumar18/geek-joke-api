# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api
import joke
import sys
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
reload(sys)
sys.setdefaultencoding('utf-8')
CORS(app)


class APP(Resource):

    def get(self):
        return {'this is soon to become an awesome->': 'website'}


    def post(self):
        jk = joke.get_joke()
        jk = jk.encode('ascii', 'ignore').decode('ascii')
        #jk = jk.encode('utf-8')
        return jk


class API(Resource):

    def get(self):
        jk = joke.get_joke()
        jk = jk.encode('ascii', 'ignore').decode('ascii')
        # jk = jk.encode('utf-8')
        return jk


api.add_resource(APP, '/')
api.add_resource(API, '/api')

if __name__ == '__main__':
    app.run(debug=False)
