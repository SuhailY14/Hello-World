#!/usr/bin/python3

import sys
import urllib
from git import Repo

def get_file_content(content):
    #Check for non-ascii in The Title
    if not content.isascii():
        print("Commit file contains non-ascii characters")
        sys.exit(1)
        
    else:
        print("VALID CONTENT")
        
if __name-- == '__main__':
    response = urllib.request.urlopen("https://github.com/SuhailY14/Hello-World/blob/BLDTLS-137/test.txt")
    content = response.read()
    content=content.decode("utf-8") 
        

    content = commit.file.content
    get_file_content(content)


