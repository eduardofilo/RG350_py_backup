# -*- coding: utf-8 -*-
import os
import logging
import settings
from configparser import ConfigParser

SEPARATOR = ','

# ConfigParser docu: https://docs.python.org/2.7/library/configparser.html
def load():
    settings.config = []
    try:
        settings.status = 0
        config_ini = ConfigParser.RawConfigParser()
        config_ini.read(settings.CONFIG_FILE)
        settings.destination_directory = config_ini.get('DEFAULT', 'destination_directory').strip()
        if not os.path.exists(settings.destination_directory):
            # We try to create destination directory
            my_cmd = "mkdir '%s'" % (settings.destination_directory)
            os.system(my_cmd)
        if not (os.path.exists(settings.destination_directory) and os.path.isdir(settings.destination_directory)):
            settings.status = 3
            raise Exception("Destination directory '%s' is not accessible." % (settings.destination_directory))
        systems = config_ini.get('DEFAULT', 'systems')
        n = 0
        for line in systems.split('\n'):
            if line:
                items = line.split(SEPARATOR)
                if len(items) < 3:
                    settings.status = 2
                    raise Exception("Line %d in config file has insuficient items." % (n+1))
                system_name = items[0].strip()
                backup_file = settings.backup_filename(system_name)
                source_available = False
                dirs = []
                for i in range(2,len(items)):
                    system_dir = items[i].strip()
                    dirs.append(system_dir)
                    source_available = source_available or os.path.exists(system_dir)
                system = {'name': system_name, 'enabled': items[1].strip() == 'True', 'backup_available': os.path.exists(backup_file), 'source_available': source_available, 'dirs': dirs}
                settings.config.append(system)
                n = n + 1
        if n == 0:
            settings.status = 1
            raise Exception("Empty file?")
    except Exception as e:
        if not settings.status:
            settings.status = 2
        logging.error('Wrong format in configuration file. ' + str(e))

def save():
    config_ini = ConfigParser.RawConfigParser()
    config_ini.set('DEFAULT', 'destination_directory', settings.destination_directory)
    systems = ""
    for system in settings.config:
        line = "\n%s,%r,%s" % (system['name'], system['enabled'], SEPARATOR.join(system['dirs']))
        systems = systems + line
        config_ini.set('DEFAULT', 'systems', systems)
    with open(settings.CONFIG_FILE, 'w') as configfile:
        config_ini.write(configfile)
