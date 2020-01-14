#!/usr/bin/python3
"""
Python script that takes in a URL,
sends a request to the URL and displays the body of the response
"""
if __name__ == '__main__':

    import urllib.request
    from sys import argv
    
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('UTF-8'))
    except urllib.error.HTTPError as error:
        print('Error code:', error.code)