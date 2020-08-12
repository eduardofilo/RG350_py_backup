# -*- coding: utf-8 -*-
import sys
import os
import pygame

# Constants
SCREEN_W = 320
SCREEN_H = 240
FPS = 15

# Vars
config = []
selected = 0
offset = 0
status = 0  # 0: NORMAL, 1: ERROR Empty config, 2: ERROR Wrong config, 3: ERROR Destionation Directory not found
            # 4: NORMAL Confirm backup, 5: NORMAL Doing backup, 6: NORMAL Confirm restore, 7: NORMAL Doing restore
system = 0
screen = None
font = None
destination_directory = ""
dev = len(sys.argv) > 1 and sys.argv[1]=='dev'
if dev:
    HOME = "/home/edumoreno/git/rg350_pystatesbackup"
    CONFIG_FILE = HOME + "/config_debug.ini"
else:
    HOME = "/media/data/local/home/.pystatesbackup"
    CONFIG_FILE = HOME + "/config.ini"
    if not os.path.exists(HOME):
        os.makedirs(HOME)
    if not os.path.exists(CONFIG_FILE):
        os.system('cp config.ini ' + CONFIG_FILE)
LOG = HOME + "/log.txt"

def backup_filename(system_name):
    system_name = system_name.replace('/', '-')
    return "%s/%s.tgz" % (destination_directory, system_name)

def n_systems_enabled():
    systems_enabled = filter(lambda system : system['source_available'] and system['enabled'], config)
    return len(systems_enabled)

def n_backups_available():
    backups_available = filter(lambda system : system['source_available'] and system['enabled'] and system['backup_available'], config)
    return len(backups_available)

def update_backup_available():
    for system in config:
        backup_file = backup_filename(system['name'])
        system['backup_available'] = os.path.exists(backup_file)

def next_backup_system(first):
    next_system = -1
    for n in range(first, len(config)):
        if config[n]['source_available'] and config[n]['enabled']:
            return n

    return next_system

def next_restore_system(first):
    next_system = -1
    for n in range(first, len(config)):
        if config[n]['source_available'] and config[n]['enabled'] and config[n]['backup_available']:
            return n

    return next_system
