::Runs the export file
::Right click this file > run as administrator
::This is required because the export command requires admin privilege

@echo off
::Go to the correct current working directory,
::since this defaults to system32 when cmd is run as admin
setlocal enableextensions
cd /d "%~dp0"

#run the program
python export.py