#!/usr/bin/python3
"""
This Python script takes a URL as input, sends a
request to that URL, and displays the value of the
'X-Request-Id' variable from the response header.
"""
import requests
import sys

if __name__ == '__main__':

    res = requests.get(sys.argv[1])
    head = res.headers.get('X-Request-Id')
    print(head)
