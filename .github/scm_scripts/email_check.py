#!/usr/bin/python3

import re
import sys
import requests
import sh
import subprocess
from git import Repo

repo = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')
