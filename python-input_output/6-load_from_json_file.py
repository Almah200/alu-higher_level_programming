#!/usr/bin/python3
'''.imported a json file.'''
import json


def load_from_json_file(filename):
    '''creating a python object from json file.'''
    with open(filename, 'r') as afile:
        json.load(afile)
