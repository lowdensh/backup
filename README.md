# backup
Easily backup files

## Setup
1. Edit backup.bat with the location of your Python executable
1. Edit config.ini:
    1. [source] path: directory containing the file you want to back up
    1. [source] file: name of the file you want to back up, including the extension
    1. [backups] path: directory where you want backups to be stored

## Usage
Simply run backup.bat, or use Windows Task Scheduler to periodically run it for you.