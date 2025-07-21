## Reddit & Twitter Topic Research Bot

This Python project lets you search Twitter and Reddit posts using either voice or text input,
filters them using NVIDIA’s LLaMA 3 (70B) for relevance, and logs the top results into a Google Sheet.

🚀 Features
🎙️ Voice and text query support

🌐 Real-time search from Reddit & Twitter

🤖 LLaMA 3 relevance filtering using NVIDIA API

📊 Google Sheets logging of top posts

✨ Clean CLI interface

```
.
├── main.py                     # Entry point of the app
├── reddit_search.py           # Reddit search logic using PRAW
├── twitter_search.py          # Twitter search logic using Tweepy
├── llama_filter.py            # Filters posts using LLaMA 3 API
├── voice_input.py             # Captures voice input using SpeechRecognition
├── sheets_writer.py           # Stores results in Google Sheets
├── config.py                  # Stores credentials and API keys
├── credentials.json           # Your Google service account key (not committed)
└── README.md
```

### ⚙️ Setup Instructions
1. Clone the Repo
```
git clone https://github.com/nairanujit3/AI-Automation-Internship-Assignment/tree/main/task%201

```
2. Install Required Packages
```
pip install -r requirements.txt
```

3. Configure config.py
Create a config.py file like this:

```
REDDIT_CLIENT_ID = "your_reddit_client_id"
REDDIT_CLIENT_SECRET = "your_reddit_client_secret"
REDDIT_USER_AGENT = "your_app_name"

TWITTER_BEARER_TOKEN = "your_twitter_bearer_token"

NVIDIA_API_KEY = "your_nvidia_api_key"

GOOGLE_SHEET_NAME = "YourGoogleSheetName"
GOOGLE_SHEETS_CREDENTIALS = "credentials.json"  # Path to your service account key
```

▶️ Run the App
```
python main.py
```
