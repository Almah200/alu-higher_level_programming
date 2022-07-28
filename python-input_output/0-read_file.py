#!/usr/bin/python3
''' Defined a function read_file.'''


def read_file(filename=""):
    '''opened a file UTF8.'''
    with open('UTF8', encoding='utf-8') as a_file:
        print(a_file.read())
