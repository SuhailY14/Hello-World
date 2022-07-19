#!/usr/bin/python3

import re
import sys
import requests
import git
from git import Repo

def get_latest_commit(repo_path, branch_path):
    repo = git.Repo(repo_path)
    for ref in repo.refs:
        if ref.path == 'refs/heads/BLDTLS-137':
            print(ref.commit.author.email)


if __name__ == '__main__':
    get_latest_commit('/mnt/home/sy/Hello-World', '')
