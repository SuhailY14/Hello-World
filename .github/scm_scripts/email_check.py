#!/usr/bin/python3

import re
import sys
import requests
import git
from git import Repo

repo = git.Repo("/mnt/home/sy/Hello-World")
commit = repo.head.commit
