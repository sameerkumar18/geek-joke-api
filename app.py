# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful import Resource, Api

import joke
import sys

app = Flask(__name__)
api = Api(app)


class App(Resource):
    def get(self):
        return {'this is soon to become an awesome->': 'website'}


class Api(Resource):
    def get(self):
        return joke.get_joke().encode('ascii', 'ignore').decode('ascii')


api.add_resource(App, '/')
api.add_resource(Api, '/api')

if __name__ == '__main__':
    app.run(debug=True)
