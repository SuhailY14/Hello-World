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
    filepath = '../../test.txt'
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        while line:
            print("Line {}: {}".format(cnt, line.strip()))
            line = fp.readline()
            cnt += 1
    
    content = line
    get_file_content(content)

    '''
    sys.path.append('../../test.txt')
    repo = Repo('../../test.txt')
    #response = urllib.request.urlopen("https://github.com/SuhailY14/Hello-World/blob/BLDTLS-137/test.txt")
    #from 'Hello-World' import test.txt


    content = r.read()
    content = content.decode("utf-8") 
        

    content = commit.file.content
    '''
    #get_file_content(content)

