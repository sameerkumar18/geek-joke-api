import json
from random import randint

from settings import JOKE_FILE


class Joke(object):
    """ Joke app
    """
    def random_digits(self, count=2):
        """ return a joke index between first
            and last joke in the data
        """
        return randint(1, count)

    def get_joke(self):
        """ return a random joke
        """
        return self._encode(self.data[self.random_digits(self.data_count)])

    def load_data(self):
        with open(JOKE_FILE) as f:
            self.data = json.load(f)

        return

    @property
    def data_count(self):
        return self.data.length

    def _encode(self, d):
        return d.encode('ascii', 'ignore').decode('ascii')
