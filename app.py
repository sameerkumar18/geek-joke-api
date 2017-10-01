# -*- coding: utf-8 -*-
from flask import Flask,request,jsonify
from flask_restful import Resource, Api
import joke
import sys
import importlib

app = Flask(__name__)
api = Api(app)

importlib.reload(sys)

@app.route('/',methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    if request.method == "GET":
        response = "this is soon to become an awesome-> : website"
        return jsonify(response)
    else:
        jk = joke.getJoke()
        jk = jk.encode('ascii', 'ignore').decode('ascii')
        #jk = jk.encode('utf-8')
        return jk

class API(Resource):
    def get(self):
        jk = joke.getJoke()
        jk = jk.encode('ascii', 'ignore').decode('ascii')
        # jk = jk.encode('utf-8')
        return jk

api.add_resource(API, '/api')

if __name__ == '__main__':
    app.run(debug=True)
