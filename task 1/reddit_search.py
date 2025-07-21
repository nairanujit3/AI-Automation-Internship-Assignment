import praw
import config

reddit = praw.Reddit(
    client_id=config.REDDIT_CLIENT_ID,
    client_secret=config.REDDIT_CLIENT_SECRET,
    user_agent=config.REDDIT_USER_AGENT
)

def search_reddit(query, limit=30):
    results = []
    for submission in reddit.subreddit("all").search(query, sort="relevance", limit=limit):
        results.append({
            "title": submission.title,
            "selftext": submission.selftext[:300],
            "url": f"https://reddit.com{submission.permalink}",
            "engagement": submission.num_comments,
            "platform": "Reddit"
        })
    return results

