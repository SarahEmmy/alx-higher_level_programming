#!/usr/bin/python3
"""
    This Python script takes GitHub credentials (username and password) 
    and utilizes the GitHub API to display your user ID
"""
import requests
import sys

if __name__ == '__main__':

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    json = r.json()
    try:
        print(json['id'])
    except:
        print("None")
