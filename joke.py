# -*- coding: utf-8 -*-
import json
from random import randint

with open('data.json', encoding='utf-8-sig') as data_file:
    data = json.load(data_file)
JOKE_COUNT = len(data)


def get_joke():
    # Return random joke
    random_num = randint(1, JOKE_COUNT)
    joke = data[random_num]
    return joke.replace('\"', "'")
