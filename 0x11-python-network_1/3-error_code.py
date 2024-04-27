#!/usr/bin/python3
"""
    this is a script that fetches a URL and displays the body
    of the response, catching errors as well
"""
from urllib import request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            print(data)
    except HTTPError as err:
        print(f"Error code: {err.code}")
