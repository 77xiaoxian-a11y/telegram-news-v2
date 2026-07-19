import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

r = requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": "🎉 GitHub 测试成功！如果你看到这条消息，说明机器人配置正确。"
    }
)

print(r.status_code)
print(r.text)
