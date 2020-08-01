from datetime import datetime as dt
import configparser
import logging
from os import path
from sys import exit
import shutil


date = dt.strftime(dt.now(), '%Y%m%d')
time = dt.strftime(dt.now(), '%H%M%S')
config = configparser.ConfigParser()
config.read('config.ini')
logging.basicConfig(filename='backup.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

try:
    source_path = config['source']['path']
    source_file = config['source']['file']
    backup_path = config['backups']['path']
except:
    logging.error('config.ini does not exist, could not be read, or is missing keys')
    exit(1)
if source_path == '' or source_file == '' or backup_path == '':
    logging.error('config.ini key without value')
    exit(1)
if not path.isdir(source_path):
    logging.error(f'source_path {source_path} does not exist or could not be read')
    exit(1)
if not path.isdir(backup_path):
    logging.error(f'backup_path {backup_path} does not exist or could not be read')
    exit(1)
original = path.join(source_path, source_file)
if not path.isfile(original):
    logging.error(f'source_file {source_file} does not exist or could not be read')
    exit(1)

backup = f'{path.join(backup_path, source_file)}.{date}.{time}.bak'
shutil.copy(original, backup)
logging.info(f'Backed up {source_file} to {backup_path}')
