#!/usr/bin/python3

import re
import sys
import requests
import sh
import subprocess
from git import Repo

def get_lastest_commit(repo_path, branch_path):
    repo = git.Repo(repo_path)
    for ref in repo.refs:
        print(ref.path)

if __name__ == '__main__':
    get_latest_commit('/mnt/home/sy/Hello-World', '')
