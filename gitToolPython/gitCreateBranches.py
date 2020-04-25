import git 
from setting import git_repos, new_branch

class Git_branches:    

    # get user input 
    def get_user_input(self, input):
        user_input = input("Insert the "+input+" \n") 
	return user_input

    # Method to create branches 
    def create_branches(self, git_repo, user, department, name):
      
        git_repo = git.Repo(repo)
        origin = self.git_repo.remote()
        current = self.git_repo.branches['DET_develop']
        current.checkout()
        self.git_repo.git.pull('origin', current)              
        self.git_repo.create_head("feature/"+department+name+user)
        feature = self.git_repo.branches["feature/"+department+name+user]  
        origin.push(new_branch)
        feature.checkout()


# Main function					
if __name__ == "__main__":	
		
    # Class instance
    Branch_creation = Git_branches()
    # calling Class methods
    user_name = Branch_creation.get_user_input("user name ex: amancini")
    department = Branch_creation.get_user_input("department name ex: EU-DET")
    name = Branch_creation.get_user_input("branch name")
    for repo in git_repos:
        Branch_creation.create_branches(repo, user_name, department, name)
        