import os
import json
import requests
import feedparser

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

RSS = [
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://rss.nytimes.com/services/xml/rss/nyt/World.xml"
]

STATE_FILE = "sent.json"

# 读取已发送记录
if os.path.exists(STATE_FILE):
    with open(STATE_FILE, "r", encoding="utf-8") as f:
        sent = json.load(f)
else:
    sent = {}

for url in RSS:
    feed = feedparser.parse(url)

    if not feed.entries:
        continue

    news = feed.entries[0]

    news_id = news.link

    # 已发送过就跳过
    if sent.get(url) == news_id:
        print("Skip:", news.title)
        continue

    text = f"""📰 {news.title}

🔗 {news.link}
"""

    r = requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

    print(r.status_code)
    print(r.text)

    if r.status_code == 200:
        sent[url] = news_id

# 保存发送记录
with open(STATE_FILE, "w", encoding="utf-8") as f:
    json.dump(sent, f)
