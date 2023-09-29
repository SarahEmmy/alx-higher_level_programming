#!/usr/bin/python3

"""
This Python script is designed to take a URL as input, send
a request to that URL, and then extract and display the value
of the 'X-Request-Id' variable located within the
response's header.
"""
import urllib.request
import sys

if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        value = response.info()
    print(value['X-Request-Id'])
