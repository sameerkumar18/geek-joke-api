# -*- coding: utf-8 -*-
import json
from random import *


def random_digits(joke_count):
    # Return a joke index between first and last joke in data
    if joke_count and joke_count >= 1:
        return [True,randint(1, joke_count)]
    return [False,"json dataset is empty"]	

def getJoke():
    # Return random joke
    with open('data.json') as data_file:
        data = json.load(data_file)
        joke = random_digits(len(data))
        if joke[0]:
	    	return data[joke[1]]
        return joke[1] 	