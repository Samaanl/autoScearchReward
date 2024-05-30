@echo off
setlocal EnableDelayedExpansion
set vminsatance=4
set stopvmlb=1
set stopvmub=!vminsatance!
set vmname=1
FOR /L %%A IN (1,1,3) DO (
    FOR /L %%B IN (1,1,!vminsatance!) DO (
        echo starting vm sam!vmname!
        set /a vmname+=1
    )
    echo "stop for 10 min"
        FOR /L %%B IN (!stopvmlb!,1,!stopvmub!) DO (
        echo stop vm sam%%B
    )
    set /a stopvmlb+=!stopvmub!
    set /a stopvmub+=!vminsatance!
    
    
)