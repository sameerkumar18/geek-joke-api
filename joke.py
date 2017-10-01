# -*- coding: utf-8 -*-
import json
from random import randint

def random_digits():
    range_start = 1
    with open('data.json') as data_file:
        data = json.load(data_file)
    range_end = len(data)
    return randint(range_start, range_end)

def getJoke():
    with open('data.json') as data_file:
        data = json.load(data_file)
    joke = data[random_digits()]
    return joke
