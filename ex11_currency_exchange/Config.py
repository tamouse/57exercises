import configparser
import os

CONFIG_FILE = os.path.join(os.environ['HOME'], '.config', 'openexchangerates.org.ini' )

class Config():
    def __init__(self):
    self.config = configparser.ConfigParser()
    self.config.read(CONFIG_FILE)
    
