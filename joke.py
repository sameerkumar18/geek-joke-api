# -*- coding: utf-8 -*-
import json
from random import randint


def get_joke():
    # Return random joke
    with open('data.json') as data_file:
        data = json.load(data_file)
    joke = data[randint(1, len(data))]
    return joke
