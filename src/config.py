import configparser
from os.path import abspath

api_token = ''

mongo_database_name = ''
mongo_url = ''

def init(conf_file = None):
    """
    A method for initializing the configuration and assigns values to the global variables.
    """
    global api_token
    global mongo_database_name
    global mongo_url
    
    config = configparser.ConfigParser()

    if conf_file == None:
        config.read(abspath("ci.ini"))
    else:
        config.read(conf_file)

    api_token = config['Notification']['api_token']

    mongo_database_name = config['Database']['name']
    mongo_url = config['Database']['url']