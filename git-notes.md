# Note for course  STAT679
## How to play with git?
1. First, I need an account for [githib](https://github.com/)
2. Create a repository (repo), I call it "yiming_STAT679",  without creating any read.md,  I will create one in local terminal  
3. Go to my laptop find a directory (folder) that will be used  to connect the repo in github, in this case, it is ~/STAT679/
4. Initialize the local directory as a Git repository by typing  `git init`

## How to do some work with git?
1. Make a file readme.md in this folder (STAT679) by typing  `touch readmd.md`
2. Go into readme.md to add some infomation about "yiming_STAT679"
3. Add readme.md to stage  `add readme.md`
4. Check the status that readme.md has been added  `git status`
5. Shoulf work, then commit it  `git commit readmel.md -m "first commit, readme.md only"`
6. Check the status again  `git status`
7. Ok now, build the connection between local folder "STAT679"  and repo "yiming_STAT679"  `git remote add origin git@github.com:yimingweng/yiming_STAT679.git`
8. Note that the "git@git..." is the SSH of repo "yiming_STAT679"
9. Let's verify the connection:  `git remote -v`
10. Ok, let's upload the current modification to github  `git push --set-upstream origin master`
11. Note that this is the first push, for the later push, just type:
>     `git push`
>Go to github, reload the webpage, and see what happen
