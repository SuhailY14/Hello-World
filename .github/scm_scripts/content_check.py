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
        
if __name__ == '__main__':
    repo = Repo('../../test.txt')
<<<<<<< HEAD
    # response = urllib.request.urlopen("https://github.com/SuhailY14/Hello-World/blob/BLDTLS-137/test.txt")
=======
    #response = urllib.request.urlopen("https://github.com/SuhailY14/Hello-World/blob/BLDTLS-137/test.txt")
>>>>>>> 1362bd4880f09d871632eb2aaa219937b4b8b5d1
    content = response.read()
    content = content.decode("utf-8") 
        

    content = commit.file.content
    get_file_content(content)

