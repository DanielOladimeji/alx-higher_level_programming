#!/usr/bin/python3
""" lists 10 commits (from the most recent to oldest) of the repository"""
import requests
import sys

if __name__ == "__main__":
    repo_owner = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10".format(repo_owner, repo)

    response = requests.get(url)
    commits = response.json()

    for commit in commits:
        sha = commit.get("sha")
        name = commit.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))

