#!/usr/bin/python3
def magic_calculation(x, y):
    result = 0

    for j in range(1, 3):
        try:
            if (j > a):
                raise Exception('Too far')
            else:
                result += x ** y / j
        except:
            result = x + y
            pass
    return (result)
