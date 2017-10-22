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
        return {'this is soon to become an awesome->': 'website'}

    def post(self):
        return joke.getJoke()


class API(Resource):
    def get(self):
        return joke.getJoke()


api.add_resource(APP, '/')
api.add_resource(API, '/api')

if __name__ == '__main__':
    app.run(debug=True)
