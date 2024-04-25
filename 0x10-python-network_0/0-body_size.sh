#!/bin/bash
# sends a request to a URL and displays the size of the the body
curl -s "$1" | wc -m

