echo "# ME470" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ma53ma/ME470.git
git push -u origin main


NOW:
git pull origin main

# If you are creating files that are not already in the GitHub:
git add _______

git commit -m "first commit"
git push -u origin main