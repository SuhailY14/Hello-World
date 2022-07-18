#!/usr/bin/python3

import re
import sys
import requests
from requests_html import HTMLSession


GITHUB_EMAIL_URL = 'https://github.com/settings/emails'

def check(email_id):
    
    headers = {
        "Authorization": "Basic ",
        "Accept": "application"
    }

    try: 
        url = 'https://api.github.com/repos/Hello-World/{0}/commits/{1}'
        f = urlopen(url)
        content = f.read()
        commits = json.loads(content.decode('utf-8'))
        return commits['sha']
    except:
        return "ERROR: Unable to retreive latest commit" 

    
if __name__ == '__main__':
    regex = "^[a-zA-Z0-9].@infoblox.com$"
    if (re.search(regex, GITHUB_EMAIL_URL)):
        print("Usage: email_check <EMAIL ID> <IS VALID>")
    else:
        print("Invalid Email ID")
    
    check(GITHUB_EMAIL_URL)
