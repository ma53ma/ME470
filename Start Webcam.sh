#!/bin/bash
#This will allow users a shortcut in MACOS to run our program (webcam)
#Currently untested need to run line in terminal:
#chmod +x ~/Desktop/myFolder/myscript.bash
cd obj_det
osascript -e 'tell app "Terminal"
    do script "python3 yolo.py --webcam==True"
end tell'
