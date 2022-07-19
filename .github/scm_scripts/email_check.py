#!/usr/bin/python3

import re
import sys
import requests
import sh
import subprocess
from git import Repo

git = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')

def get_git_revisions_hash():
    hashes = []
    hashes.append(subprocess.check_output(['git', 'rev-parse', 'HEAD']))
    hashes.append(subprocess.check_output(['git', 'rev-parse', 'HEAD^']))
    return hashes
