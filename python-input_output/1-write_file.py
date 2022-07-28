#!/usr/bin/python3
'''defined a function.'''


def write_file(filename="", text=""):
    ''' opened a file for writing.'''
    with open(filename, mode='w', encoding = 'utf-8') as almah:
        return almah.write(text)
