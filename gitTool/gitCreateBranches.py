import git 
from setting import git_repos, new_branch

for repo in git_repos:
    git_repo = git.Repo(repo)
    origin = git_repo.remote()
    current = git_repo.branches['DET_develop']
    git_repo.git.pull('origin', current)    
    feature = git_repo.branches[new_branch]    
    git_repo.create_head(new_branch)
    origin.push(new_branch)
    feature.checkout()