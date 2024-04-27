#!/usr/bin/python3
"""
    this is a script that sends a request to a URL and displays
    the value of the X-Request-Id variable found in the header
    of the response
"""
if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        print(headers['X-Request-Id'])
