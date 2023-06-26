#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

x = 12
y = 2
result = safe_print_division(x, y)
print("{:d} / {:d} = {}".format(x, y, result))

x = 12
y = 0
result = safe_print_division(x, y)
print("{:d} / {:d} = {}".format(x, y, result))
