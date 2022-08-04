#!/usr/bin/python3

import sys
import urllib
import tempfile
import os
from git import Repo

def get_file_content(content):
    #Check for non-ascii in The Title
    if not content.isascii():
        print("Commit file contains non-ascii characters")
        sys.exit(1)

    else:
        print("VALID CONTENT")

if __name__ == '__main__':
    filepath = 'Hello-World'
    #filepath = '../../'
    repo = Repo(filepath)

    commits_list = list(repo.iter_commits(max_count=1))

    commit = commits_list[0]

    print("commit id:", commit)

    filename = repo.git.show("--pretty=",'--name-only', commit)
    print("file name:", filename)
    
    #filecontent = repo.git.show("%s:%s" % (commit, filename))
    #print(filecontent)
    
    filelocation = '../../'
    location = filelocation + filename
    print(location)
    with open(location) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
    
    content = line
    get_file_content(content)

