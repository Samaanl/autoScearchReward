@echo off
setlocal EnableDelayedExpansion
set vmnum=1
set vmname=sam
::how many vm want to run at a time you have mention the number here
set vminsatance=4
::upper bound of vm to stop
set vmstopub=!vminsatance!
::lowwer bound of vm to start
set vmstoplb=1


FOR /L %%A IN (1,1,2) DO (
    FOR /L %%B IN (1,1,!vminsatance!) DO (
        VBoxManage startvm "!vmname!!vmnum!"
        C:\Windows\System32\timeout.exe /t 10



:: Run the good.sh script inside the VM
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
    

    


:: the VMs will run for 1900 seconds
C:\Windows\System32\timeout.exe /t 1900

    :: closing the vm
    FOR /L %%C IN (!vmstoplb!,1,!vmstopub!) DO (
        echo closing vm !vmname!%%C
        VBoxManage controlvm "!vmname!%%C" savestate

    )
    set /a vmstoplb+=!vmstopub!
    set /a vmstopub+=!vminsatance!

)
