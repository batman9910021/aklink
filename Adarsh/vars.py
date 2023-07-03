# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '5574912'))
    API_HASH = str(getenv('API_HASH', '37f90ccb92ff182cd707b3516d20ac3b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6340019631:AAFL3Wl8IsA7baGw8vhg5Ja59J32D1QRWJU'))
    name = str(getenv('name', 'ImaxLink_Bot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '3'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1001936581912'))
    PORT = int(getenv('PORT', 3389))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '195.154.237.14'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6269004803").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Batman_0'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', '195.154.237.14:3389')) if not ON_HEROKU or getenv('FQDN', '195.154.237.14:3389') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://sksie00:sksie00@cluster0.m1nej3h.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'Akimaxmovies_0'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())) 
