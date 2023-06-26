#!/usr/bin/python3
def safe_print_division(x, y):
    try:
        c = x / y

    except (ZeroDivisionError, TypeError, ValueError):
        c = None

    finally:
        print("Inside result: {}".format(c))

    return (c)
