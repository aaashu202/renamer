import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", ""))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBots")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")

# config.py

WEBHOOK = True  # ✅ Enable webhook mode
WEBHOOK_URL = "https://your-app-name.render.com"  # 🌐 Your hosted bot URL (no slash at end)
PORT = 8080  # 🔌 Default port used by Render/Heroku/Railway
