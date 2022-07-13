#!/usr/bin/python3

import re
import requests


GITHUB_EMAIL_URL = 'https://github.com/settings/emails'

def check(email_id):
    
    headers = {
        "Authorization": "Basic ",
        "Accept": "application"
    }

    try: 
        url = GITHUB_EMAIL_URL
        response = requests.request("GET", url)
        if response.status_code == 200:
            print("EMAIL Response: ", response.get('key'))
            return True
        else:
            print("EMAIL error occurred: ", response.text)
            return False
    except Exception as e:
        print("EMAIL Exception occurred ", str(e))
        return False

    return False


if __name__ == '__main__':
    x = "^[a-zA-Z0-9].@infoblox.com$"
    if (re.search(x, GITHUB_EMAIL_URL)):
        print("Valid Infoblox Email ID")
    else:
        print("Invalid Email ID")
