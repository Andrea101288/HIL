import os
import git 
from setting import git_repos, feature_branches

# Define Class
class Git_update:
	
	# define method to update and merge 2 branches
	def update_and_merge(self, git_repo, feature_branch, main_branch):
		#Inizialize git repo
		repo = git.Repo(git_repo)
		# get current branch
		if feature_branch in repo.branches:
			current  =  repo.branches[feature_branch]
		else:
			print(feature_branch+" does't exist")
			quit()			
		# try to pull from remote feature branch, if the remote branch doesn't exist yet skip this step
		try:
			repo.git.pull('origin', current)			
		except:
			pass
		
		for submodule in repo.submodules:
			submodule.update(init=True)

		# get Main branch 
		if main_branch in repo.branches:
			main = repo.branches[main_branch]
			repo.git.pull('origin', main)
			for submodule in repo.submodules:
				submodule.update(init=True)
			# find the merge base of these two branches
			base = repo.merge_base(current, main)
			# stage a merge operation
			repo.index.merge_tree(main, base=base)
			# commit changes, providing links to the two parent commits
			repo.index.commit('Merge '+main_branch+' into '+feature_branch+"'", parent_commits=(current.commit, main.commit))	 
			current.checkout(force=True)
			repo.git.pull('origin', main)
			repo.git.pull('origin', current)
			# push the merged branch to remote, if it doesn't exist yet create it
			try:
				repo.git.push(current)
			except:
				repo.git.push('--set-upstream', 'origin', current)
		else:
			print(main_branch+"doesn't exist")	
			quit()

# Main function					
if __name__ == "__main__":
	# create the class object
	Gitool = Git_update()
	for repo in git_repos:
		print("\n------"+repo+"------\n")
		# call the funcion
		Gitool.update_and_merge(repo, "DET_develop", "develop")
		print("Update branch develop merged into DET_develop")
		# merge DET_develop in every feature branch you have 
		for branch in feature_branches:
			Gitool.update_and_merge(repo, branch, "DET_develop")
			print("Update branch DET_develop merged into "+branch)	
	
		print("All git folder branches Merging complete!")
        