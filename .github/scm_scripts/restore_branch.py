from subprocess import check_output
import sys
from git import Repo

def get_deleted_branch():
    deleted_branch = []
    raw_results = repo.git.reflog(max_count=1)
    #print(raw_results)
    all_words = raw_results.split('\n')
    for i in all_words:
        if 'checkout:' in i and 'main' not in i:
            all = i.split()
            deleted_branch.append(all[5])
    return deleted_branch

def restore_branch(deleted_branch, sha):
    return check_output('git checkout -b %s' % deleted_branch % sha, shell=True).strip()

if __name__ == '__main__':
    filepath = '../../'
    repo = Repo(filepath)
    '''
    sha = repo.git.reflog(max_count=1)
    all_words = sha.split()
    first_word = all_words[0]
    print("sha:", first_word)
    '''
    sha = []
    log = repo.git.reflog(max_count=1)
    #print(log)
    all_words = log.split('\n')
    for i in all_words:
        all = i.split()
        sha.append(all[0])
    print("sha:", sha)

    dry_run = '--yes' not in sys.argv
    deleted_branch = get_deleted_branch()
    for deleted_branch in get_deleted_branch():
        if dry_run:
            print(deleted_branch)
        else:
            print(restore_branch(deleted_branch, sha))
    if dry_run:
        print('*******************************************')
        print('Pass in --yes to restore the deleted branch')
        print('*******************************************')
