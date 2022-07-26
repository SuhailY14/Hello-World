#!/usr/bin/python3

import sys
from git import Repo

def get_file_content(content):
    #Check for non-ascii in The Title
    if not content.isascii():
        print("Commit file contains non-ascii characters")
        sys.exit(1)
        
    else:
        print("VALID CONTENT")
        
if __name-- == '__main__':
    repo= Repo('../../')
    with open(repo) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
        

    content = commit.file.content
    get_file_content(content)


