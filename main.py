import os
import requests
import feedparser

print("NEWS VERSION 1.0")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

RSS = [
    ("BBC", "https://feeds.bbci.co.uk/news/world/rss.xml"),
    ("New York Times", "https://rss.nytimes.com/services/xml/rss/nyt/World.xml")
]

for source, url in RSS:
    print(f"Checking: {source}")

    feed = feedparser.parse(url)

    if not feed.entries:
        print(f"{source}: No news found")
        continue

    news = feed.entries[0]

    text = (
        f"📰 {source}\n\n"
        f"{news.title}\n\n"
        f"🔗 {news.link}"
    )

    r = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text,
            "disable_web_page_preview": False
        }
    )

    print(f"{source}: {r.status_code}")
    print(r.text)
