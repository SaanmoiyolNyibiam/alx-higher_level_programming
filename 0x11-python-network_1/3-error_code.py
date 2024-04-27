#!/usr/bin/python3
"""
    this is a script that fetches a URL and displays the body
    of the response, catching errors as well
"""
if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    url = argv[1]
    try:
        with request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            print(data)
    except error.HTTPError as err:
        print(f"Error code: {err.code}")
