#!/usr/bin/python3
"""
This Python script fetches the content of the 'https://intranet.hbtn.io/status' URL
"""
import requests

if __name__ == '__main__':

    res = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
