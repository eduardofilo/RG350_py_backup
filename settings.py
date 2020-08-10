import sys
import os
import logging
import pygame

# Constants
SCREEN_W = 320
SCREEN_H = 240
FPS = 15
SEPARATOR = ','

def init():
    global config
    global screen
    global font

    config = []

    if len(sys.argv) > 1 and sys.argv[1]=='debug':
        HOME = "/home/edumoreno/git/rg350_pystatesbackup"
    else:
        HOME = "/media/data/local/home/.pystatesbackup"
    if not os.path.exists(HOME):
        os.makedirs(HOME)
    LOG = HOME + "/log.txt"
    CONFIG = HOME + "/config.txt"
    if not os.path.exists(CONFIG):
        os.system('cp config.txt ' + CONFIG)

    logging.basicConfig(level=logging.DEBUG, filename=LOG, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")

    try:
        file  = open(CONFIG, 'r')
        for line in file:
            items = line[:-1].split(SEPARATOR)
            system = {'name': items[0], 'enabled': items[1] == 'True', 'dirs': []}
            for i in range(2,len(items)):
                system['dirs'].append(items[i])
            config.append(system)
    except:
        pass
