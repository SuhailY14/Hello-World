#!/usr/bin/python3

import re
import sys
import sh
import os
from git import Repo

repo = Repo(' /mnt/home/sy/Hello-World')

commits_list = list(repo.iter_commits())
for i in range(1):
    print(commit.author.email)
