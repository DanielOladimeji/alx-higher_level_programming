#!/usr/bin/python3
""" script takes your GitHub credentials (username and password) and
uses the GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    input_username = sys.argv[1]
    input_password = sys.argv[2]
    auth = HTTPBasicAuth(input_username, input_password)
    response = requests.get("https://api.github.com/user", auth=auth)
    user_id = response.json().get('id')
    print(user_id)
