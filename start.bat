@ECHO OFF
FOR /F "delims=: tokens=2" %%a in ('ipconfig ^| find "IPv4"') do set _IPAddress=%%a
cd /d %~dp0 & "env\Scripts\activate" & python manage.py runserver 192.168.10.101:80
cmd /k