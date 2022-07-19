#!/usr/bin/python3

import re
import sys
import requests
import sh
from git import Repo


git = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')

print ("%s" % git.log[0])
