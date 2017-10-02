# -*- coding: utf-8 -*-
import json
from random import *


def random_digits(length):
    range_start = 1
    return randint(range_start, length)


def getJoke(file='data.json'):
    """
    Returns a random joke from file.
    """
    with open(file) as data_file:
        data = json.load(data_file)
        l = len(data_file)
    joke = data[random_digits(l)]
    print joke
    return joke


if __name__ == "__main__":
    getJoke():
