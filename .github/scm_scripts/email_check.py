#!/usr/bin/python3

import re
import sys
import sh
import git
import os
from git import Repo

COMMITS_TO_PRINT = 5




#def get_latest_commit(repo_path, branch_path):
#   for ref in repo.refs:
 #       if ref.path == 'refs/heads/BLDTLS-137':
  #          print(ref.commit.author.email)


