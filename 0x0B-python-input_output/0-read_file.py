#!/usr/bin/python3
""" Read and print a text file (UTF-8) to stdout """


def read_file(filename=""):
    """ Read UTF-8 file and print its contents"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
