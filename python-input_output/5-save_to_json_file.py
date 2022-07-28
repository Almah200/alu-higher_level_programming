#!/usr/bin/python3
''' imported a json file-writing function.'''
import jason


def save_to_json_file(my_obj, filename):
    '''write and object to a text file using a json representation.'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
