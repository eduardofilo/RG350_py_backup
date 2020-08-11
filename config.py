# -*- coding: utf-8 -*-
import os
import logging
import settings
import ConfigParser

SEPARATOR = ','

# ConfigParser docu: https://docs.python.org/2.7/library/configparser.html
def init():
    try:
        settings.error = 0
        config_ini = ConfigParser.RawConfigParser()
        config_ini.read(settings.CONFIG_FILE)
        systems = config_ini.get('DEFAULT', 'systems')
        n = 0
        for line in systems.split('\n'):
            if line:
                items = line.split(SEPARATOR)
                if len(items) < 3:
                    settings.error = 2
                    raise Exception("Line %d in config file has insuficient items." % (n+1))
                system = {'name': items[0].strip(), 'enabled': items[1].strip() == 'True', 'dirs': []}
                for i in range(2,len(items)):
                    if os.path.exists(items[i].strip()):
                        system['dirs'].append(items[i].strip())
                if len(system['dirs']) > 0:
                    settings.config.append(system)
                n = n + 1
        if n == 0:
            settings.error = 1
            raise Exception("Empty file?")
    except Exception as e:
        if not settings.error:
            settings.error = 2
        logging.error('Wrong format in configuration file. ' + str(e))

def save():
    config_ini = ConfigParser.RawConfigParser()
    systems = ""
    for system in settings.config:
        line = "\n%s,%r,%s" % (system['name'], system['enabled'], SEPARATOR.join(system['dirs']))
        systems = systems + line
        config_ini.set('DEFAULT', 'systems', systems)
    with open(settings.CONFIG_FILE, 'wb') as configfile:
        config_ini.write(configfile)
