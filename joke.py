# -*- coding: utf-8 -*-
import json
import random


def random_digits(item_count):
    return random.randint(0, item_count)


def get_joke():
    with open('data.json') as data_file:
        data = json.load(data_file)
    return data[random_digits(len(data))]
