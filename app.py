# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api
import joke
import sys

app = Flask(__name__)
api = Api(app)
reload(sys)
sys.setdefaultencoding('utf-8')


class APP(Resource):

    def get(self):
    # function is called when the user makes a GET request to / endpoint.
        return {'this is soon to become an awesome->': 'website'}


class API(Resource):

    def get(self):
    # function is called when the user makes a GET request to /api endpoint.    
        jk = joke.getJoke()
        jk = jk.encode('ascii', 'ignore').decode('ascii')
        return jk


api.add_resource(APP, '/')
api.add_resource(API, '/api')

if __name__ == '__main__':
    app.run(debug=True)
