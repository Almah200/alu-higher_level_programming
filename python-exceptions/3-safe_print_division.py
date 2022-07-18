#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        return a / b
    except exception:
        return None
    finally:
        print('{}'.format(safe_print_division(a / b))
