import os


from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AVAILABLE_TOKENS = os.getenv("AVAILABLE_TOKENS")