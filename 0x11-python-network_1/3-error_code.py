#!/usr/bin/python3
"""
This Python script sends a request to a provided URL
while handling HTTP errors.
"""
import urllib.request
import sys

if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(req) as res:
            reqst = res.read().decode('utf8')
        print(reqst)

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
