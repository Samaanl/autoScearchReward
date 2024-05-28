@echo off
setlocal EnableDelayedExpansion
set vmnum=1
set vmstopnum=1
set vmname=sam
set PASSWORD=2004

FOR /L %%A IN (1,1,2) DO (
    FOR /L %%A IN (1,1,4) DO (
        @REM echo starting vm !vmname!!vmnum!
        VBoxManage startvm "!vmname!!vmnum!"
        C:\Windows\System32\timeout.exe /t 10
        @REM running the good.sh script

@REM echo pressed pass
@REM VBoxManage controlvm "!vmname!!vmnum!" keyboardputstring "%PASSWORD%"
@REM C:\Windows\System32\timeout.exe /t 5
@REM echo pressed enter 
@REM VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 1c
@REM VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 9c

:: Run the good.sh script inside the VM
        @REM C:\Windows\System32\timeout.exe /t 10
        echo Running good.sh script...
        ::1D 38 14 are press singnal for ctrl + alt + T
        VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 1D 38 14
        ::9D B8 94 are release singnal for ctrl + alt + T
        VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 9D B8 94

        C:\Windows\System32\timeout.exe /t 5
        VBoxManage controlvm "!vmname!!vmnum!" keyboardputstring "cd Desktop/vmproject"
        ::1c press and 9c release enter button
        VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 1c
        VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 9c

        C:\Windows\System32\timeout.exe /t 5


        VBoxManage controlvm "!vmname!!vmnum!" keyboardputstring "./good.sh"
        VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 1c
        VBoxManage controlvm "!vmname!!vmnum!" keyboardputscancode 9c



        set /a vmnum+=1
    )
    

    



 C:\Windows\System32\timeout.exe /t 1900
    @REM closing the vm
    @REM echo stopping vm !vmname!!vmstopnum!
    VBoxManage controlvm "!vmname!!vmstopnum!" savestate
    set /a vmstopnum+=1
    @REM echo stopping vm !vmname!!vmstopnum!
    VBoxManage controlvm "!vmname!!vmstopnum!" savestate
    set /a vmstopnum+=1


)
