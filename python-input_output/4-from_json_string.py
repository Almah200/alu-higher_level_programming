#!/usr/bin/python3
'''.imported json.'''
import json


def from_json_string(my_str):
    '''return the python object representatio of json.'''
    return json.loads(my_str)
