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
        url = 'https://github.com/settings/emails'
        session = HTMLSession()
        r = session.get('https://github.com/settings/emails')
        if r == 200:
            print("EMAIL Response: ", r.get('key'))
            return True
        else:
            print("EMAIL error occurred: ", r.text)
            return False
    except Exception as e:
        print("EMAIL Exception occurred ", str(e))
        return False

    return False


if __name__ == '__main__':
    regex = "^[a-zA-Z0-9].@infoblox.com$"
    if (re.search(regex, GITHUB_EMAIL_URL)):
        print("Usage: email_check <EMAIL ID> <IS VALID>")
    else:
        print("Invalid Email ID")
    
    check(GITHUB_EMAIL_URL)

