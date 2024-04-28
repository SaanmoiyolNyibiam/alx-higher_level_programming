#!/usr/bin/python3
""" this is a script that fetches https://alx-intranet.hbtn.io/status """
if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    data = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(data.text)}")
    print(f"\t- content: {data.text}")
