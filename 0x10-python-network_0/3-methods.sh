#!/bin/bash
# this is a script that displays all HTTP methods a server acceps
curl -sI $1 | grep "Allow" | cut -d ":" -f 2
