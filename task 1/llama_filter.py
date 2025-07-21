import requests
import time
import config  # contains NVIDIA_API_KEY

LLAMA_ENDPOINT = "https://integrate.api.nvidia.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {config.NVIDIA_API_KEY}",
    "Content-Type": "application/json"
}

def is_relevant(post, query):
    prompt = f"""
You are an intelligent assistant. A user searched for:
→ "{query}"

Now determine if the following post is relevant to that search.
Such that the important words in the search should be there.
Post:
Platform: {post.get("platform", "Unknown")}
Title: "{post.get('title', '')}"
URL: {post.get("url", "")}

Only answer with "True" or "False". Do not explain.
"""

    body = {
        "model": "meta/llama3-70b-instruct",
        "messages": [{"role": "user", "content": prompt}]
    }

    try:
        response = requests.post(LLAMA_ENDPOINT, headers=HEADERS, json=body)
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"].strip().lower()
        return "true" in answer
    except Exception as e:
        print("⚠️ LLaMA API failed:", e)
        return False


def filter_posts(posts, query, delay_sec=1.2):
    """
    Filters a list of post dictionaries based on relevance to the query using LLaMA.
    Each post should have: 'title', 'url', 'platform'
    """
    filtered = []
    for i, post in enumerate(posts, 1):
        print(f"🔍 Checking post {i}/{len(posts)}: {post['title'][:80]}...")
        try:
            if is_relevant(post, query):
                print("✅ Relevant")
                filtered.append(post)
            else:
                print("⛔️ Irrelevant")
        except Exception as e:
            print("⚠️ Failed to check post:", e)
        time.sleep(delay_sec)  # avoid rate limits

    return filtered
