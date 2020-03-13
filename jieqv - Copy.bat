findstr /i /C:"Update ID   :" *.log > 1.txt
setlocal enabledelayedexpansion
rem for /f "tokens=*" %%i in ('type 1.txt') do (
for /f "tokens=*" %%i in ('type 1.txt') do (
set str=%%i
echo !str:~100!>>2.txt
) 
rem del 1.txt