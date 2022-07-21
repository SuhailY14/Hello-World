#!/usr/bin/python3

import sys
import re
import sh
from git import Repo
 
regex = "^[a-zA-Z0-9]*.@infoblox.com$"

def check_author_email(email):
    if (re.fullmatch(regex, email)):
        print("VALID DOMAIN NAME")
        sys.exit(0)
        
    else:
        print("author.email=",email)
        print("Author Email ID format: [a-zA-Z0-9].@infoblox.com")
        sys.exit(0)

    
if __name__ == '__main__':
    #repo = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World') 
    repo= Repo('../../')
    commits_list = list(repo.iter_commits(max_count=1))

    commit = commits_list[0]
    '''
    author = repo.git.log( "--pretty='%ae'", "-n 1")
    print(author.email)
    author_email = author.email
    if len(sys.argv) < 2:
        print("Usage: email_check <pusher email>")
        sys.exit(1)

    author_email = sys.argv[1]
    '''
    email = commit.author.email
    check_author_email(email)
