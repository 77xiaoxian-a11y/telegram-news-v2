import os
import feedparser
import requests
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=BOT_TOKEN)

# 这里填写RSS
RSS_FEEDS = [
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
    "https://feeds.bbci.co.uk/news/world/rss.xml",
]

def send(text):
    bot.send_message(chat_id=CHAT_ID, text=text)

def main():
    for url in RSS_FEEDS:
        feed = feedparser.parse(url)

        if not feed.entries:
            continue

        news = feed.entries[0]

        title = news.title
        link = news.link

        message = f"📰 {title}\n\n{link}"

        send(message)

if __name__ == "__main__":
    main()
