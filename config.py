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
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://STRenameBot:STRenameBot@cluster0.p7bubb0.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "madflixbotz")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")

# config.py

WEBHOOK = False  # ✅ Enable webhook mode
WEBHOOK_URL = "https://mysterious-beatrix-bhankharvansh-2b1eb8fb.koyeb.app"  # 🌐 Your hosted bot URL (no slash at end)
PORT = 8000  # 🔌 Default port used by Render/Heroku/Railway
