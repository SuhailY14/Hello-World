#!/usr/bin/python3

import re
import sys
import requests
import sh
import subprocess
from git import Repo

def author(self):
    repo = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')
    commits_list = list(repo.iter_commits(1))
    
    commit = commits_list[1]
    
    author = repo.git.show("-s", "--format=%ae", commit.hexsha)
    print(commit.hexsha)
    print(author)
