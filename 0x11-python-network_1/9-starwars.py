#!/usr/bin/python3
"""
Script that takes in a string and sends
a search request to the Star WarsAPI
"""

import requests
from sys import argv


if __name__ == "__main__":
    arg = ""
    if len(argv) == 2:
        arg = argv[1]
    try:
        req = requests.get('https://swapi.co/api/people/?search={}'.format(arg))
        js = req.json()
        if js:
            print('Number of results:', js['count'])
            for i in js.get('results'):
                print(i.get('name'))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')