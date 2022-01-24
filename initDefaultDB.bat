@echo off
setlocal
set currentPath=%~dp0
REM DO NOT FORGET!!! activate virtualenv
call %currentPath%tg2env/Scripts/activate.bat
cd PZ5
call "../tg2env/Scripts/gearbox.exe" setup-app
endlocal
pause