#!/usr/bin/python3

import re
import sys
import requests
import sh
import subprocess
from git import Repo

def author(self):
    repo = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')
    commits_list = list(repo.iter_commits())
    
    for i in range(5):
        commit = commits_list[i]
        
        author = repo.git.show("-s", "--format=Author: %an <%ae>", commit.hexsha)
        print(author)
