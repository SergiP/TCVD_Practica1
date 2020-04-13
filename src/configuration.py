import configparser

class Configuration:
    def __init__(self,nameFile):
        config = configparser.RawConfigParser()
        config.read('config.properties')
        self.nameFile = nameFile
        self.web = config.get('Web', 'web.url')  

    def get_url(self):
        return self.web