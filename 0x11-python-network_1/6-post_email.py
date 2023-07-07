#!/usr/bin/python3
""" Takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body"""
import sys
import requests


if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=value)
    print(r.text)
