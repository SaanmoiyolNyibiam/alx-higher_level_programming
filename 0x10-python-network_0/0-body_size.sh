#!/usr/bin/bash
# this is a script that takes in a URL, sends a request to that
# URL, and displays the size of the body of the response

URL="$1"
curl -s "$URL" | wc -m

