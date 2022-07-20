#!/usr/bin/python3

import sys
import re
import sh
from git import Repo
 
regex = "^[a-zA-Z0-9].@infoblox.com$"

def check_author_email(self, email):
    if (re.fullmatch(regex, author_email)):
        print("VALID DOMAIN NAME")
        sys.exit(0)
        
    else:
        print(“author email format: '[a-zA-Z0-9].@infoblox.com' ”)
        sys.exit(1)
        
    repo = sh.git.bake(_cwd= '/mnt/home/sy/Hello-World')
    commits_list = list(repo.iter_commits(1))
    
    commit = commits_list[1]
    
    author = repo.git.log( "--pretty='%ae'", "-n 1")
    print(author.email)

    
if __name__ == '__main__':
   author_email = author.email 
   if len(sys.argv) < 2:
        print("Usage: email_check <pusher email>")
        sys.exit(1)

    title = sys.argv[1]
    check_pusher_email(email)
