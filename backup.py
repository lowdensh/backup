from datetime import datetime as dt
import configparser
from os import path
from sys import exit
import shutil


date = dt.strftime(dt.now(), '%Y%m%d')
time = dt.strftime(dt.now(), '%H%M%S')

config = configparser.ConfigParser()
config.read('config.ini')

try:
    source_path = config['source']['path']
    source_file = config['source']['file']
    backup_path = config['backups']['path']
except:
    print('Error: config.ini: does not exist, could not be read, or is missing keys')
    exit(1)

if source_path == '' or source_file == '' or backup_path == '':
    print(f'Error: config.ini: key without value')
    exit(1)
if not path.isdir(source_path):
    print(f'Error: config.ini: source_path {source_path} does not exist or could not be read')
    exit(1)
if not path.isdir(backup_path):
    print(f'Error: config.ini: backup_path {backup_path} does not exist or could not be read')
    exit(1)

original = path.join(source_path, source_file)
if not path.isfile(original):
    print(f'Error: config.ini: source_file {source_file} does not exist or could not be read')
    exit(1)

backup = f'{path.join(backup_path, source_file)}.{date}.{time}.bak'
shutil.copy(original, backup)
