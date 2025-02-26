@echo off
cd /d C:\Users\setia\etl_project
call venv\Scripts\activate
python load.py > etl_log.txt 2>&1