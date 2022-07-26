#!/usr/bin/python3
def repeat(word, n, sep=', '):
    return sep.join(word for _ in range(n))
