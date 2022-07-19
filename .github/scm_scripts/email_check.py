#!/usr/bin/python3

import re
import sys
import requests
import sh
import subprocess
from git import Repo

git = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')

commits_list = list(Repo.iter_commits())

for i in range(5):
    commit = commits_list[i]

   
    print(commit.author)
