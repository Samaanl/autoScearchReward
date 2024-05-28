@echo off
setlocal EnableDelayedExpansion
set VM_NAME=sam4
set PASSWORD=2004

:: Start the VM with the VirtualBox GUI
echo starting vm
VBoxManage startvm "%VM_NAME%"

:: Wait for the VM to fully start (adjust the timeout as needed)
timeout /t 30

:: Send the password to the VM
timeout /t 5
echo pressed pass
VBoxManage controlvm "%VM_NAME%" keyboardputstring "%PASSWORD%"
timeout /t 5
echo pressed enter 
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 1c
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 9c

:: Run the good.sh script inside the VM
timeout /t 10
echo Running good.sh script...
::1D 38 14 are press singnal for ctrl + alt + T
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 1D 38 14
::9D B8 94 are release singnal for ctrl + alt + T
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 9D B8 94

timeout /t 5
VBoxManage controlvm "%VM_NAME%" keyboardputstring "cd Desktop/vmproject"
::1c press and 9c release enter button
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 1c
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 9c

timeout /t 5


VBoxManage controlvm "%VM_NAME%" keyboardputstring "./good.sh"
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 1c
VBoxManage controlvm "%VM_NAME%" keyboardputscancode 9c


:: Optional: Pause the script to keep the VM running
pause




