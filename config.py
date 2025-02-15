import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7340598359:AAFDepKwg945PvRIqNeENqfJB-TyeBRFvpk")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28920407"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "999f6cf8b866224b2741f36b5b44d777")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://shaurykumar21:B42KPhWMkhslv50D@cluster0.2lhp5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
