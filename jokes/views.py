from flask_restful import Resource
from .joke import Joke


class JokeView(Joke, Resource):
    """ Joke page view
    """
    def get(self, *args, **kwargs):
        return self.get_joke()


class JokeAPI(Joke, Resource):
    """ Joke API endpoint
    """
    def get(self, *args, **kwargs):
        return self.get_joke()