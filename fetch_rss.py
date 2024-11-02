import feedparser
import json

# RSSフィードのURL
RSS_URL = "https://note.com/kuwaharu/rss"
MAX_ITEMS = 5  # 最大取得件数

# RSSフィードをパース
feed = feedparser.parse(RSS_URL)

# エラーチェック
if feed.bozo:
    print("Failed to parse RSS feed:", feed.bozo_exception)
    exit(1)

articles = []

# 最新の記事を取得
for entry in feed.entries[:MAX_ITEMS]:
    articles.append(
        {
            "title": entry.title,
            "link": entry.link,
            "published": entry.published,
            "summary": entry.summary,
            "creator_name": entry.get("creatorName", ""),
            "creator_image": entry.get("creatorImage", ""),
        }
    )

# JSONファイルの書き込み
with open("latest_articles.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"Successfully fetched {len(articles)} articles.")
