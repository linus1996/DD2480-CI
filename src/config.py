import configparser
from os.path import abspath

api_token = ''

mongo_database_name = ''
mongo_ip = ''
mongo_port = ''
mongo_user = ''
mongo_pass = ''

def init(conf_file = None):
    global api_token
    global mongo_database_name
    global mongo_ip
    global mongo_port
    global mongo_user
    global mongo_pass
    
    config = configparser.ConfigParser()

    if conf_file == None:
        config.read(abspath("ci.ini"))
    else:
        config.read(conf_file)

    api_token = config['Notification']['api_token']

    mongo_database_name = config['Database']['name']
    mongo_ip = config['Database']['ip']
    mongo_port = config['Database']['port']
    mongo_user = config['Database']['user']
    mongo_pass = config['Database']['password']