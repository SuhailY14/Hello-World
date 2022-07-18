#!/usr/bin/python3

import re
import sys
import requests
from git import Repo


GITHUB_EMAIL_URL = 'https://api.github.com/repos/Hello-World/{0}/commits/{1}'

def check(email_id):

    try: 
        url = 'https://api.github.com/repos/Hello-World/{0}/commits/{1}'
        f = urlopen(url)
        content = f.read()
        commits = json.loads(content.decode('utf-8'))
        return commits['sha']
    except:
        return "ERROR: Unable to retreive latest commit" 
 
    
