#!/usr/bin/python3

import re
import sys
import requests
import sh
import subprocess
from git import Repo

def author(self):
    git = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')
    commits_list = list(git.iter_commits())
    
    for i in range(5):
        commit = commits_list[i]
        
        print(commit.author)
