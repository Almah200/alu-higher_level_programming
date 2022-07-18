#!/usr/bin/python3
try:
def safe_print_list(my_list=[], x=0):
    for x in my_list:
        print(x, end='')
except NameError:
    print("x is not defined")

