#!/usr/bin/python3
"""
    this is a script that takes in a letter,
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter,
"""
from requests import post, exceptions
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]
    params = {'q': q}

    # if the response body is not properly JSON formatted and empty
    # if the response body is properly JSON formatted and not empty
    try:
        response = post(url, params)
        data = response.json()
        if not data:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except exceptions.RequestException:
        print("Not a valid JSON")

