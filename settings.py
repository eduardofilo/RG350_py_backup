# -*- coding: utf-8 -*-
import sys
import os
import logging
import pygame

# Constants
SCREEN_W = 320
SCREEN_H = 240
FPS = 15
SEPARATOR = ','

# Vars
config = []
selected = 0
screen = None
font = None
debug = len(sys.argv) > 1 and sys.argv[1]=='debug'

def init():
    global config
    if debug:
        HOME = "/home/edumoreno/git/rg350_pystatesbackup"
        CONFIG = HOME + "/config_debug.txt"
    else:
        HOME = "/media/data/local/home/.pystatesbackup"
        CONFIG = HOME + "/config.txt"
        if not os.path.exists(HOME):
            os.makedirs(HOME)
        if not os.path.exists(CONFIG):
            os.system('cp config.txt ' + CONFIG)
    LOG = HOME + "/log.txt"

    logging.basicConfig(level=logging.DEBUG, filename=LOG, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")

    try:
        file  = open(CONFIG, 'r')
        n = 0
        for line in file:
            items = line[:-1].split(SEPARATOR)
            if len(items) < 3:
                raise Exception("Line %d in config file has insuficient items." % (n+1))
            system = {'name': items[0], 'enabled': items[1] == 'True', 'dirs': []}
            for i in range(2,len(items)):
                if os.path.exists(items[i]):
                    system['dirs'].append(items[i])
            if len(system['dirs']) > 0:
                config.append(system)
            n = n + 1
        if n == 0:
            raise Exception("Empty file?")
    except Exception as e:
        config = []
        logging.error('Wrong format in configuration file. ' + str(e))
    finally:
        file.close()
