REM @echo off
setlocal
set dependencies=tg.devtools
set currentPath=%~dp0
REM create virtualenv if not exist
if not exist "%currentPath%tg2env" (
    call virtualenv tg2env
)
REM DO NOT FORGET!!! activate virtualenv
echo "Activating enviroment"
call %currentPath%tg2env/Scripts/activate.bat
echo "Installing devtools"
call %currentPath%tg2env/Scripts/pip install %dependencies%
echo "Installing dependencies"
cd pz5
call %currentPath%tg2env/Scripts/pip install -e .
endlocal
pause