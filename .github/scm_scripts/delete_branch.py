from subprocess import check_output
import sys
from git import Repo


def get_merged_branches():
    ''' a list of merged branches, not couting the current branch or main '''
    raw_results =  check_output(b'git branch --merged main', shell=True)
    raw_results = raw_results.decode()
    #print(raw_results)
    return [b.strip() for b in raw_results.split('\n')
        if b.strip() and not b.startswith('*') and b.strip() != 'main']


def delete_branch(branch):
    return check_output('git branch -D %s' % branch, shell=True).strip()
'''
def restore_branch(branch):
    return check_output('git checkout -b %s' % branch % commit, shell=True).strip()
'''
if __name__ == '__main__':
    dry_run = '--confirm' not in sys.argv
    for branch in get_merged_branches():
        if dry_run:
            print(branch)
        else:
            print(delete_branch(branch))
    if dry_run:
        print('*****************************************************************')
        print('Did not actually delete anything yet, pass in --confirm to delete')
        print('*****************************************************************')
    '''
    filepath = '../../'
    repo = Repo(filepath)

    commits_list = list(repo.iter_commits(max_count=1))

    commit = commits_list[0]

    print("commit id:", commit)

    dry_run = '--yes' not in sys.argv
    for branch in get_merged_branches():
        if dry_run:
            print(branch)
        else:
            print(restore_branch(branch))
    if dry_run:
        print('*******************************************')
        print('Pass in --yes to restore the deleted branch')
        print('*******************************************')
    '''
