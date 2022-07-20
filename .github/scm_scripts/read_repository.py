import os
import git
from git import Repo

remoteurl= "git@github.com:SuhailY14/Hello-World.git"
localfolder= " /mnt/home/sy"

myrepo = git.Repo('/mnt/home/sy/Hello-World')


COMMITS_TO_PRINT = 5

def print_commit_data(commit):
    print('-----')
    print(str(commit.hexsha))
    print("\"{}\" by {} ({})".format(commit.summary, commit.author.name, commit.author.email))
    print(str(commit.authored_datetime))
    print(str("count: {} and size: {}".format(commit.count(), commit.size)))


