#!/usr/bin/python3

import re
import sys
import requests
import sh
import git
from git import Repo

def get_latest_commit(repo_path, branch_path):
    repo = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')
    for ref in repo.refs:
        if ref.path == 'refs/heads/BLDTLS-137':
            print(ref.commit.author.email)


