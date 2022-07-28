#!/usr/bin/python3
''' Defined a function read_file.'''


def read_file(filename=""):
    '''opened a file UTF8.'''
    with open('UTF8', mode='r', encoding='utf-8') as a_file:
        a_file.read()
