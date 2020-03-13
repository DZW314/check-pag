del 0supslist.txt
for %%i in (*.uxz) do call: haha

:haha
set "str=%%~ni"
:intercept
if "%str:~-1%"==" " set "str=%str:~0,-1%"&goto intercept
@echo str >> 44.txt
goto:efo

for %%i in (*.tgz) do @echo %%~ni >> 0supslist.txt
for %%i in (*.bin) do @echo %%~ni >> 0supslist.txt
for %%i in (*.uxz) do @echo %%~ni >> 0supslist.txt