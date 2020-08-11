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
config_enabled = []
selected = 0
offset = 0
status = 0  # 0: NORMAL, 1: ERROR Empty config, 2: ERROR Wrong config, 3: ERROR Destionation Directory not found, 4: NORMAL Confirm backup
            # 5: NORMAL Doing backup
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
