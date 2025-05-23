import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler

#Recommended
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8114490677:AAFhdHq28T8K0WKhqvZKL7lvF8c8MFw6DBg")
APP_ID = int(os.environ.get("APP_ID", "27382214"))
API_HASH = os.environ.get("API_HASH", "6a3913eb3f026ab02e7ac1c420df2ad0")

##---------------------------------------------------------------------------------------------------

#Main 
OWNER_ID = int(os.environ.get("OWNER_ID", "5984303934"))
PORT = os.environ.get("PORT", "8010")

##---------------------------------------------------------------------------------------------------

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Links:Links@cluster0.07koqod.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Links")

##---------------------------------------------------------------------------------------------------

#Default
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))
START_MSG = os.environ.get("START_MESSAGE", "") #No Need keep it blank
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5984303934").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

##---------------------------------------------------------------------------------------------------        

#Default
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = None

##---------------------------------------------------------------------------------------------------

#Admin == OWNERID
ADMINS.append(OWNER_ID)
ADMINS.append(5984303934)

##---------------------------------------------------------------------------------------------------

#Default
LOG_FILE_NAME = "links-sharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
##---------------------------------------------------------------------------------------------------
