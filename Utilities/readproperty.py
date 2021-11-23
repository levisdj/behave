import os
from pathlib import Path
import configparser, sys
config = configparser.RawConfigParser()
configFilePath = './Configuration/config.ini'

try:
    config.read(configFilePath)
except Exception as e:
    print(str(e))


# path = Path(__file__)
# ROOT_DIR = path.parent.absolute()
# config_path = os.path.join(ROOT_DIR, "config.ini")

# config = configparser.ConfigParser()
# config.read(config_path)


class ReadConfig:
    @staticmethod
    def getURL():
        # url = None
        try:
            url = config.get('common-info', 'baseURL')
            return url
        except Exception as ex:
            print(str(ex), 'couldn\'t read configuration file')
        # return url

    @staticmethod
    def getUserName():
        username = config.get('common-info', 'userName')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common-info', 'password')
        return password
