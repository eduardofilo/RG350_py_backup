import logging  #logging.debug(string)


class Config():
    SEPARATOR = ','
    config = []

    def __init__(self, config_file):
        try:
            file  = open(config_file, 'r')
            for line in file:
                items = line[:-1].split(self.SEPARATOR)
                system = {'name': items[0], 'enabled': items[1], 'dirs': []}
                for i in range(2,len(items)):
                    system['dirs'].append(items[i])
                self.config.append(system)
        except:
            pass
