@ECHO OFF
set service_name=%1
set exe_name=%2

if "%service_name%"=="" (
    echo need service_name as arg1
    pause
    exit
)

if "%exe_name%"=="" (
    echo need service_name as arg2
    pause
    exit
)

net stop %service_name%>NUL 2>&1

sc delete %service_name% > NUL 2>&1

%~dp0/instsrv.exe %service_name% %~dp0/srvany.exe>NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo create service failed!
    echo Perhaps need authorized!
    pause
    exit
) else (
    echo create service success!
)

REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\%service_name%\Parameters /v Application /f /d "%~dp0%exe_name%">NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo register program failed!
    echo Perhaps need authorized!
    pause
    exit
) else (
    echo register program success!
)

REG ADD HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\%service_name%\Parameters /v AppDirectory /f /d "%~dp0\">NUL 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo register program path failed!
    echo Perhaps need authorized!
    pause
    exit
) else (
    echo register program path success!
)

net start %service_name%