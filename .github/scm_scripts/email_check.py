import git 
from git import Repo

my_repo = git.Repo('Hello-World')

commits_list = list(repo.iter_commits())

for i in range(5):
    commit = commits_list[i]

    print(commit.hexsha)
    print(commit.author)
    print(commit.committer)
