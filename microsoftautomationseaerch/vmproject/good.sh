#!/bin/bash

python3 vmscript.py

#it requires 610 sec to comeplete the vmscript 
#sleep 620

python3 vmmobile.py

#xdotool is to bind hotkey in bash script

sleep 5

xdotool key alt+F4
sleep 0.3
xdotool keyup alt+F4
xdotool key alt+F4
sleep 0.3
xdotool keyup alt+F4
sleep 1
#Return is pressing enter button
xdotool key Return
sleep 0.3
xdotool keyup Return
