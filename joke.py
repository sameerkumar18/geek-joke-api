# -*- coding: utf-8 -*-
import json
from random import randint


def getJoke():
    # return a random joke loaded from the data.json
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data[randint(0, len(data) - 1)]
