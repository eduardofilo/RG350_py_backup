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
error = 0   # 1: Empty config, 2: Wrong config
screen = None
font = None
destination_directory = ""
debug = len(sys.argv) > 1 and sys.argv[1]=='debug'
if debug:
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
