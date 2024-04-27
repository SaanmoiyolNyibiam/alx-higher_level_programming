#!/usr/bin/python3
"""
    this is a script that fetches a URL and displays the body
    of the response, catching errors as well
"""
from urllib import request, error
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            print(data)
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
