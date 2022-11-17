#!/usr/bin/python3

import sys
import magic
import mimetypes
import os
from git import Repo

def get_file_content(content):
    flag = 0
    for i in content:
        #Check for non_ascii characters in text files
        if not i.isascii():
            print("Commit file contains non-ascii characters")
            sys.exit(1)
        else:
            flag += 1

    if flag != 0:
        print("Valid Content, Commit file doesn't contain non-ascii characters")

if __name__ == '__main__':
    filepath = os.path.realpath("../../dryrun_nios/dryrun_nios/")
    #print("filepath:", filepath)

    repo = Repo(filepath, search_parent_directories=True)
    #print("repo:", repo)

    commits_list = list(repo.iter_commits(max_count=1))

    commit = commits_list[0]

    print("commit id:", commit)

    filename = repo.git.show("--pretty=",'--name-only', commit)
    all_files = filename.split('\n')
    print("file names:", all_files)

    for i in all_files:
        File_Type = magic.from_file(i, mime=True).split('\n')
        print("File Type:", File_Type)
        for i in File_Type:
            if not 'text/' in i:
                print("Only text Files are Executable")
                sys.exit(1)

    location = ["../../dryrun_nios/dryrun_nios/"+x for x in all_files]
    #print("location:", location)

    content = []
    for i in location:
        with open(i, "r") as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt, line.strip()))
                content.append(line.strip())
                line = fp.readline()
                cnt += 1

    get_file_content(content)
