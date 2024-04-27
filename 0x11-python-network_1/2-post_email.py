#!/usr/bin/python3
"""
    this is a script that sends a POST request to a passed URL
    with an email as a parameter, and displays the body of
    the response(decoded in utf-8)
"""
if __name__ == "__main__":
    from urllib import request, parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    params = {"email": email}
    data = parse.urlencode(params).encode('utf-8')
    req = request.Request(url, data, method='POST')
    with request.urlopen(req) as response:
        response = response.read()
        print(response.decode('utf-8'))
