from reddit_search import search_reddit
from twitter_search import search_twitter
from llama_filter import filter_posts
from voice_input import listen_for_query
from sheets_writer import store_in_sheets
from sheets_writer import store_in_sheets

def get_user_query():
    print("🔍 Choose input method:")
    print("1. 🎙️ Voice")
    print("2. ⌨️ Type")
    
    choice = input("Enter 1 for voice, 2 for typing: ").strip()

    if choice == '1':
        query = listen_for_query()
        if query:
            return query
        else:
            print("⚠️ Voice input failed. Please type instead.")
            return input("Enter your search query: ").strip()
    elif choice == '2':
        return input("Enter your search query: ").strip()
    else:
        print("❌ Invalid choice. Exiting.")
        exit()

def main():
    query = get_user_query()
    if not query:
        print("❌ No query provided. Exiting.")
        return

    print(f"\n🔎 Searching for: {query}\n")

    # Fetch data
    reddit_posts = search_reddit(query)
    twitter_posts = search_twitter(query)

    # Combine and filter
    all_posts = reddit_posts + twitter_posts
    filtered_posts = filter_posts(all_posts, query)

    # Display
    if not filtered_posts:
        print("😔 No relevant posts found.")
    else:
        print(f"\n✅ Top {min(len(filtered_posts), 10)} relevant posts:\n")
        for i, post in enumerate(filtered_posts[:10], 1):
            print(f"{i}. {post['title']}")
            print(f"🔗 {post['url']}\n")
            
        store_in_sheets(filtered_posts)
        print("📤 Results pushed to Google Sheets!")

if __name__ == "__main__":
    main()
