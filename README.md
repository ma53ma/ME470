# Initial terminal lines to enter to add the github to a local folder (I think)
echo "# ME470" >> README.md  
git init  
git add README.md  
git commit -m "first commit"  
git branch -M main  
git remote add origin https://github.com/ma53ma/ME470.git  
git push -u origin main  


# Terminal lines to enter after github is added
git pull origin main

// If you are creating files that are not already in the GitHub:  
git add ______

git commit -m "first commit"
git push -u origin main
