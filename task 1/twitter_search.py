import tweepy
import config

client = tweepy.Client(bearer_token=config.TWITTER_BEARER_TOKEN)

def search_twitter(query, max_results=10, require_engagement=True):
    results = []
    try:
        response = client.search_recent_tweets(
            query=f'"{query}" lang:en -is:retweet',
            max_results=max_results,
            tweet_fields=["public_metrics", "lang"]
        )

        if not response.data:
            return results

        for tweet in response.data:
            if tweet.lang != "en":
                continue

            metrics = tweet.public_metrics
            engagement = metrics.get("retweet_count", 0) + metrics.get("like_count", 0)

            if require_engagement and engagement == 0:
                continue

            results.append({
                "platform": "Twitter",
                "title": tweet.text.replace('\n', ' ')[:100], 
                "url": f"https://twitter.com/i/web/status/{tweet.id}",
                "engagement": engagement
            })

        results.sort(key=lambda x: x["engagement"], reverse=True)

    except Exception as e:
        print(f"[Twitter Error] {e}")

    return results
