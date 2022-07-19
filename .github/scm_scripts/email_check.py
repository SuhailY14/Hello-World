#!/usr/bin/python3

import re
import sys
import requests
import subprocess
import git
from git import Repo

def get_latest_commit(repo_path, branch_path):
    repo = git.Repo(repo_path)
    for ref in repo.refs:
        if ref.path == 'refs/heads/BLDTLS-137':
            print(ref.commit)
            print(ref.commit.author.email)

regex = "^[a-zA-Z0-9].@infoblox.com$"

if(re.search(regex, get_latest_commit)):
    print("EAMIL ID IS VALID")
else:
    print("INVALID EMAIL ID")

    

if __name__ == '__main__':
    get_latest_commit('/mnt/home/sy/Hello-World', '')
