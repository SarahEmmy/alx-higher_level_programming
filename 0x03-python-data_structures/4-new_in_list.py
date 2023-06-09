#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if idx < len(my_list) and idx >= 0 and len(my_list) != 0:
        new_list[idx] = element
    return new_list
