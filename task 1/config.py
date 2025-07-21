# config.py
from dotenv import load_dotenv
import os

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
GOOGLE_SHEETS_CREDENTIALS = os.getenv("GOOGLE_SHEETS_CREDENTIALS")
GOOGLE_SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME", "Topic Research")
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
