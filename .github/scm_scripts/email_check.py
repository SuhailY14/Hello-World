#!/usr/bin/python3

import re
import sys
import requests
import os
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
 
    commit = commits_list[1]
       
    author = repo.git.show("-s", "--format=Author: %an <%ae>", commit.hexsha)
    print(author)
    
    regex = "^[a-zA-Z0-9].@infoblox.com$"
    if (re.search(regex, author)):
        print("Usage: email_check <EMAIL ID> <IS VALID>")
    else:
        print(" Invalid Email ID")



