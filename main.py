import os
import requests
import feedparser

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

RSS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://feeds.bbci.co.uk/news/world/rss.xml",
]

for url in RSS:
    feed = feedparser.parse(url)

    if not feed.entries:
        continue

    news = feed.entries[0]

    text = f"📰 {news.title}\n\n{news.link}"

    r = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    print(r.status_code)
    print(r.text)
