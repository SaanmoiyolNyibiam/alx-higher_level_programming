#!/bin/bash
# this is a script that displays all HTTP methods a server acceps
curl -sI "$1" | grep -i "^allow" | cut -d " " -f 2-
