@echo off
setlocal
set dependencies=tg.devtools
set currentPath=%~dp0
REM create virtualenv if not exist
if not exist "%currentPath%tg2env" (
    call virtualenv tg2env
)
REM DO NOT FORGET!!! activate virtualenv
call %currentPath%tg2env/Scripts/activate.bat
call %currentPath%tg2env/Scripts/pip install %dependencies%
call %currentPath%tg2env/Scripts/pip install -e .
endlocal
pause