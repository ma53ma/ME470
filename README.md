# Initial terminal lines to enter to add github to a local folder
cd to folder you want github to be added to  
git init  
git remote add origin https://github.com/ma53ma/ME470.git  

# Terminal lines to enter after github is added
git pull origin main

// If you are creating files that are not already in the GitHub, add their names into underline (ex. run_yolo.py)  
git add ______

git commit -m "first commit"  
git push -u origin main

# Lines to enter if you run into issues with the above lines
git pull origin main --allow-unrelated-histories  

git add ____________  

git commit -m "commit message here"  

git push origin HEAD:main  




# Links that code is pulled from to create this repository 
[1] https://blog.roboflow.com/training-a-yolov3-object-detection-model-with-a-custom-dataset/ 
[2] https://towardsdatascience.com/object-detection-using-yolov3-and-opencv-19ee0792a420?gi=82dd13e620a9 
