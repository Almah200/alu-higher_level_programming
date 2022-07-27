#!/usr/bin/python3
'''. created a function.'''


def is_same_class(obj, a_class):
    ''' instantiated isinstance method.'''
    result = isinstance(obj, a_class)
    if result:
        print('Yes')
    else:
        print('No')
