# -*- coding: utf-8 -*-
import json
from random import randint


def random_digits(joke_count):
    # Return a joke index between first and last joke in data
    return randint(1, joke_count)

def get_joke():
    # Return random joke
    with open('data.json') as data_file:
        data = json.load(data_file)
    joke = {"joke" : data[random_digits(len(data))]}
    return joke
