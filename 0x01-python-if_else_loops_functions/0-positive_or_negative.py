#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number < 0:
    print('{:d}'.format(number) + ' is negative')
elif number > 0:
    print('{:d}'.format(number) + ' is positive')
else:
    print('{:d}'.format(number) + ' is zero')
