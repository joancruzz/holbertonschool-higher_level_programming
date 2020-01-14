#!/usr/bin/python3
"""
Python script that takes your Github credentials
and uses the Github API to display your id
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    req = requests.get('https://api.github.com/user',
                       auth=(argv[1], argv[2]))
    print(req.json().get('id'))
