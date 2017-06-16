# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api
import joke
import sys


app = Flask(__name__)
api = Api(app)



reload(sys)
sys.setdefaultencoding('utf-8')

class API(Resource):
    def get(self):
        return {'this is should become a ->': 'website'}

    def post(self):
        jk = joke.getJoke()
        jk = jk.encode('ascii', 'ignore').decode('ascii')
        #jk = jk.encode('utf-8')
        return jk

api.add_resource(API, '/')

if __name__ == '__main__':
    app.run(debug=True)
