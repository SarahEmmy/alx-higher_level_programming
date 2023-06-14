#!/usr/bin/python3
def complex_delete(dictionary, value):
    for key in list(dictionary.keys()):
        if dictionary[key] == value:
            del dictionary[key]
    return dictionary
