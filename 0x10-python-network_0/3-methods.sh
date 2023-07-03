#!/bin/bash
# This Bash script takes in a URL and displays all HTTP methods the server will accept
curl -s -i "$1" | grep "Allow:" | cut -d " " -f2-
