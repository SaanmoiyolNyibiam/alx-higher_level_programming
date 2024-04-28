#!/usr/bin/python3
"""
    this is a script that sends a request to a passed URL,
    and displays the body of the response.
    - if the status code >= 400, it prints it
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    data = get(url)
    if data.status_code >= 400:
        print(f"Error code: {data.status_code}")
    else:
        print(data.text)
