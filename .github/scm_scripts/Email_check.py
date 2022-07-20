#!/usr/bin/python3

import sys
import requests

token = "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"

REPO_URL = 'https://api.github.com/repods/SuhailY14/Hello-World/'

def get_commit_author():

    headers = {
        "Authorization": "token ".format(token)
    }

    try:
        url = REPO_URL+commit_id
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            print("REPO Response: ", response.json().get('key'))
            return True
        else:
            print("REPO error occurred: ", response.text)
            return False
    except Exception as e:
        print("REPO Exception occurred ", str(e))
        return False

    return False


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: Email_check <REPO COMMIT ID> <token>")
        sys.exit(1)

    commit = sys.argv[1]
    token = sys.argv[2]

    ret = False
    ret = repo(commit, token)

    if ret:
        sys.exit(0)
    else:
        sys.exit(1)
