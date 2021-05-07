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




# Links that code is pulled from to create this repository and anything else we used
packages used: cv2,numpy,argparse,time
language used: Python
Here opencv is used alongside yolo for object detection using image processing.

Sources:
[1] https://towardsdatascience.com/object-detection-using-yolov3-and-opencv-19ee0792a420?gi=82dd13e620a9
This blog post provides a tutorial that teaches beginners how to get started interfacing OpenCV with YOLOv3. This tutorial provides you with the necessary Python libraries to run YOLOv3 as well as example code and functions of YOLOv3 in use.  
[2] https://blog.roboflow.com/training-a-yolov3-object-detection-model-with-a-custom-dataset/  
This blog post is home to the Google Colab notebook that was used at the beginning of this semester to train YOLOv3 using a custom dataset. While the team shifted away from YOLOv3 during this semester, this link is helpful to further understand the process of training object detection algorithms.  
[3] https://www.tutorialspoint.com/batch_script/batch_script_syntax.htm  
Guide for writing scripts to run commands in Windows 10.  
