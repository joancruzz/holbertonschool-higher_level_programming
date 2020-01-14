#!/usr/bin/python3
"""
Send a POST request to the passed URL with the email
as a parameter, and displays the body of the response
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)
