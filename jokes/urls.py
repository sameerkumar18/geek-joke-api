from app import application
from .views import JokeView, JokeAPI


api = Api(application)


api.add_resource(JokeView, '/')
app.add_resource(JokeAPI, '/api')