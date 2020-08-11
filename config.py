# -*- coding: utf-8 -*-
import os
import logging
import settings

def init():
    SEPARATOR = ','
    try:
        file  = open(settings.CONFIG_FILE, 'r')
        n = 0
        for line in file:
            items = line[:-1].split(SEPARATOR)
            if len(items) < 3:
                raise Exception("Line %d in config file has insuficient items." % (n+1))
            system = {'name': items[0].strip(), 'enabled': items[1].strip() == 'True', 'dirs': []}
            for i in range(2,len(items)):
                if os.path.exists(items[i].strip()):
                    system['dirs'].append(items[i].strip())
            if len(system['dirs']) > 0:
                settings.config.append(system)
            n = n + 1
        if n == 0:
            raise Exception("Empty file?")
    except Exception as e:
        settings.config = []
        logging.error('Wrong format in configuration file. ' + str(e))
    finally:
        file.close()
