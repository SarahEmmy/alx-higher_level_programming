#!/usr/bin/python3
import random
num  = random.randint(-10, 10)
if num < 0:
    print('{:d}'.format(num) + ' is negative')
elif num > 0:
    print('{:d}'.format(num) + ' is positive')
else:
    print('{:d}'.format(num) + ' is zero')
