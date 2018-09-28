# Note for course  STAT679
## Using git to organize files and works
How to start playing with git?
- First, I need an account for [githib](https://github.com/)
- Create a repository (repo), I call it "yiming_STAT679",  without creating any read.md,  I will create one in local terminal  
- Go to my laptop find a directory (folder) that will be used  to connect the repo in github, in this case, it is ~/STAT679/
- Initialize the local directory as a Git repository by typing  `git init`

How to do some work with git?
- Make a file readme.md in this folder (STAT679) by typing<br/>  `touch readmd.md`
- Go into readme.md to add some infomation about "yiming_STAT679"
- Add readme.md to stage<br/>  `add readme.md`
- Check the status that readme.md has been added<br/>  `git status`
- Shoulf work, then commit it  `git commit readmel.md -m "first commit, readme.md only"`
- Check the status again<br/>  `git status`
- Ok now, build the connection between local folder "STAT679"  and repo "yiming_STAT679"  `git remote add origin git@github.com:yimingweng/yiming_STAT679.git`
- Note that the "git@git..." is the SSH of repo "yiming_STAT679"
- Let's verify the connection:  `git remote -v`
- Ok, let's upload the current modification to github<br/>  `git push --set-upstream origin master`
- Note that this is the first push, for the later push, just type:<br/>  `git push`
- Go to github, reload the webpage, and see what happen
