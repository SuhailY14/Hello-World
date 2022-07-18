from git import Repo

repo_path = 'mockito'
repo = Repo(repo_path)

commits_list = list(repo.iter_commits())

for i in range(5):
    commit = commits_list[i]

    print(commit.hexsha)
    print(commit.author)
    print(commit.committer)
