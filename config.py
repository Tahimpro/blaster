import os 
from telethon import TelegramClient

# Ensure your API credentials are strings
API_ID = os.environ.get("API_ID", "16531092")
API_HASH = os.environ.get("API_HASH", "b073b97bd4c8c56616fc2cbbd4da845a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7843096547:AAHzkh6gwbeYzUrwQmNlskzft6ZayCRKgNU")

assert isinstance(API_ID, str), "API_ID must be a string"
assert isinstance(API_HASH, str), "API_HASH must be a string"
assert isinstance(BOT_TOKEN, str), "BOT_TOKEN must be a string"

# Initialize the client
client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Add your bot's functionality here
