#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 123:
            upper = chr(ord(c) - 32)
            c = upper
        print("{}".format(c), end="")
    printi()
