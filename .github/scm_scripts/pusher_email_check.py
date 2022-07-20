#!/usr/bin/python3

import sys
import re
import sh
from git import Repo
 
regex = "^[a-zA-Z0-9].@infoblox.com$"

def check_author_email(email, author):
    if (re.fullmatch(regex, author_email)):
        print("VALID DOMAIN NAME")
        sys.exit(0)
        
    else:
        print("Author Email ID format: [a-zA-Z0-9].@infoblox.com")
        sys.exit(0)

    
if __name__ == '__main__':
    repo = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')
    commits_list = list(repo.iter_commits())

    commit = commits_list[1]

    author = repo.git.log( "--pretty='%ae'", "-n 1")
    print(author.email)
    author_email = author.email 
    if len(sys.argv) < 2:
        print("Usage: email_check <pusher email>")
        sys.exit(1)

    author_email = sys.argv[1]
    check_author_email(email, author)
