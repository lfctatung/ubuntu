This directory is created by clone ubuntu from GitHub my account...

C:\Users\leochang\Documents\Leon>git clone --recursive https://github.com/lfctatung/ubuntu
Cloning into 'ubuntu'...
remote: Enumerating objects: 173, done.
remote: Total 173 (delta 0), reused 0 (delta 0), pack-reused 173
Receiving objects: 100% (173/173), 87.33 KiB | 835.00 KiB/s, done.
Resolving deltas: 100% (36/36), done.

C:\Users\leochang\Documents\Leon>

GitHub is a git Server for SCCS 
We can git clone it to a local folder and do the git work on the folder/repository... 
and git push... back to the Server GitHub.

C:\Users\leochang\Documents\Leon>cd ubuntu 
// ubuntu is the local folder map to the GitHub ubuntu repository/project

C:\Users\leochang\Documents\Leon\ubuntu>dir
 Volume in drive C is OSDisk
 Volume Serial Number is 92D2-BA4F

 Directory of C:\Users\leochang\Documents\Leon\ubuntu

12/30/2019  03:02 PM    <DIR>          .
12/30/2019  03:02 PM    <DIR>          ..
12/30/2019  03:01 PM                 0 anyDummy
12/30/2019  03:01 PM                36 dev
12/30/2019  03:01 PM                37 file1
12/30/2019  03:01 PM             1,192 findReDirect
12/30/2019  03:01 PM            63,682 gitConfigSetUp
12/30/2019  03:01 PM            62,707 gitConfigSetUpOld
12/30/2019  03:01 PM                27 gitDO
12/30/2019  03:01 PM               135 gitPull.txt
12/30/2019  03:01 PM            46,375 leon
12/30/2019  03:01 PM    <DIR>          my_project.git
12/30/2019  03:01 PM                31 README
12/30/2019  03:01 PM                 9 README.md
12/30/2019  03:02 PM                 0 ReadMe.txt
12/30/2019  03:01 PM                 0 READMEdummy
12/30/2019  03:01 PM                93 result
12/30/2019  03:01 PM               287 Sum.py
12/30/2019  03:01 PM               316 sumPosTuple.py
12/30/2019  03:01 PM    <DIR>          work
              16 File(s)        174,927 bytes
               4 Dir(s)  332,140,118,016 bytes free

C:\Users\leochang\Documents\Leon\ubuntu>git branch
* master

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ReadMe.txt

nothing added to commit but untracked files present (use "git add" to track)

C:\Users\leochang\Documents\Leon\ubuntu>git add ReadMe.txt // Add the newly created file

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ReadMe.txt // Untracked => Tracked after Add


C:\Users\leochang\Documents\Leon\ubuntu>del Leon  // File Deleted

C:\Users\leochang\Documents\Leon\ubuntu>notepad gitPull.txt // File Modified

C:\Users\leochang\Documents\Leon\ubuntu>git pull 
Already up to date.
// This means there is no change on Server master branch 
// can do fast-forward or linear merge.

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ReadMe.txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   gitPull.txt
        deleted:    leon


C:\Users\leochang\Documents\Leon\ubuntu>git rm leon	//	File Removed
rm 'leon'

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ReadMe.txt
        deleted:    leon

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   gitPull.txt


C:\Users\leochang\Documents\Leon\ubuntu>git add gitPull.txt	//	File Add

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   ReadMe.txt
        modified:   gitPull.txt	//	Ready to be committed
        deleted:    leon


C:\Users\leochang\Documents\Leon\ubuntu>git commit *  // Committed successfully
[master 146db14] Modified gitPull.txt, created ReadMe.txt and deleted Leon.
 Committer: Leon Chang <leon.chang@non.keysight.com>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 3 files changed, 7 insertions(+), 868 deletions(-)
 create mode 100644 ReadMe.txt  // New files
 delete mode 100644 leon

C:\Users\leochang\Documents\Leon\ubuntu>git add ReadMe.txt

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   ReadMe.txt 	// Edited

C:\Users\leochang\Documents\Leon\ubuntu>git commit -m "ReadMe.txt changed 1:21pm" ReadMe.txt
[master a36c563] ReadMe.txt changed 1:21pm
 1 file changed, 272 insertions(+)

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

C:\Users\leochang\Documents\Leon\ubuntu>git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 2.31 KiB | 2.31 MiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/lfctatung/ubuntu
   146db14..a36c563  master -> master

C:\Users\leochang\Documents\Leon\ubuntu>git merge master master
Already up to date.
C:\Users\leochang\Documents\Leon\ubuntu>git checkout -b branch2
Switched to a new branch 'branch2'

C:\Users\leochang\Documents\Leon\ubuntu>git branch
* branch2
  master

// grep (findstr) the "git " commands to see their command sequence 
// in this ReadMe.txt file...
	      ======================================================
C:\Users\leochang\Documents\Leon\ubuntu>findstr /R /c:"git " ReadMe.txt
C:\Users\leochang\Documents\Leon>git clone --recursive https://github.com/lfctatung/ubuntu
GitHub is a git Server for SCCS
We can git clone it to a local folder and do the git work on the folder/repository...
and git push... back to the Server GitHub.
C:\Users\leochang\Documents\Leon\ubuntu>git branch
C:\Users\leochang\Documents\Leon\ubuntu>git status
  (use "git add <file>..." to include in what will be committed)
nothing added to commit but untracked files present (use "git add" to track)
C:\Users\leochang\Documents\Leon\ubuntu>git add ReadMe.txt // Add the newly created file
C:\Users\leochang\Documents\Leon\ubuntu>git pull // means there is no change on Server
C:\Users\leochang\Documents\Leon\ubuntu>git status
  (use "git restore --staged <file>..." to unstage)
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
C:\Users\leochang\Documents\Leon\ubuntu>git rm leon     //      File Removed
C:\Users\leochang\Documents\Leon\ubuntu>git add gitPull.txt     //      File Add
C:\Users\leochang\Documents\Leon\ubuntu>git status
  (use "git restore --staged <file>..." to unstage)
C:\Users\leochang\Documents\Leon\ubuntu>git commit *
    git config --global --edit
    git commit --amend --reset-author
	      ======================================================
C:\Users\leochang\Documents\Leon\ubuntu>git branch -a
* branch2
  master
  remotes/origin/HEAD -> origin/master
  remotes/origin/foo2
  remotes/origin/master

C:\Users\leochang\Documents\Leon\ubuntu>git branch -m robust // Rename branch2 to robust

C:\Users\leochang\Documents\Leon\ubuntu>git branch
  master
* robust

C:\Users\leochang\Documents\Leon\ubuntu>git status
On branch robust
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ReadMe.txt

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\leochang\Documents\Leon\ubuntu>
C:\Users\leochang\Documents\Leon\ubuntu>git remote
origin

C:\Users\leochang\Documents\Leon\ubuntu>


