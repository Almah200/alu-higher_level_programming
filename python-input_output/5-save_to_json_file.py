#!/usr/bin/python3
''' imported json.'''
import jason


def save_to_json_file(my_obj, filename):
    '''.openining a file for writing.'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
