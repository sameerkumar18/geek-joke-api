# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

import joke

app = Flask(__name__)
api = Api(app)

CORS(app)


class APP(Resource):

    def get(self):
        return jsonify({
            'author': 'Sameer Kumar',
            'author_url': 'https://www.sameerkumar.website',
            'base_url': 'https://geek-jokes.sameerkumar.website',
            'project_name': 'Geek Joke API',
            'project_url': 'https://github.com/sameerkumar18/geek-joke-api'
        })

    def post(self):
        jk = joke.get_joke()
        if request.args.get('format') == 'json':
            return {'joke': jk}
        else:
            # Making sure existing clients don't break
            return jk


class API(Resource):

    def get(self):
        jk = joke.get_joke()
        if request.args.get('format') == 'json':
            return {'joke': jk}
        else:
            # Making sure existing clients don't break
            return jk


api.add_resource(APP, '/')
api.add_resource(API, '/api')

if __name__ == '__main__':
    app.run(debug=False)
