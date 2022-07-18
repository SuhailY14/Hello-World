#!/usr/bin/python3

import re
import sys
import requests
from requests_html import HTMLSession


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
    
    for i in range(1):
    commits = commits_list[i]

    print(commit.hexsha)
    print(commit.author)
    print(commit.committer)


    
if __name__ == '__main__':
    regex = "^[a-zA-Z0-9].@infoblox.com$"
    if (re.search(regex, commit.author)):
        print("Usage: email_check <EMAIL ID> <IS VALID>")
    else:
        print(" Invalid Email ID")
    
    check(GITHUB_EMAIL_URL)
