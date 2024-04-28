#!/usr/bin/python3
"""
    this is a script that takes in a URL and email,
    sends a POST request to the URL with the email a parameter,
    then displays the body of the response.
"""
from requests import post
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    params = {'email': email}

    data = post(url, params)
    print(data.text)
