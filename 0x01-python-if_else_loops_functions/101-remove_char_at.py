#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0:
        return string
    newstring = string[:n] + string[n + 1:]
    return '{:s}'.format(newstring)
