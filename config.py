import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7636817360:AAGOn8HKiYLsP2C5X8pQk70_NRhg8s2xa2w")
    APP_ID = int(os.environ.get("APP_ID", '28991562'))
    API_HASH = os.environ.get("API_HASH", '215d93eeacd3d1c704887f80b0b914f4' )
    USER_NAME = os.environ.get("USER_NAME", "")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6107997458").split())
    BANNED_USER = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    BOT_PWD = os.environ.get("BOT_PASSWORD", "itsmebarath")
    LOGGED_USER = []
    DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://rlx10:rlx100@cluster77.mgtl0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster77")
