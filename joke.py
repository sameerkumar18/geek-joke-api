# -*- coding: utf-8 -*-
import json
from random import *

def random_digits():
    range_start = 1
    range_end = 545
    return randint(range_start, range_end)
def getJoke():
    with open('data.json') as data_file:
        data = json.load(data_file)
    joke = data[random_digits()]
    print joke
    return joke