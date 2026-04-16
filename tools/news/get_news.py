# get_news.py
# ================================================
# Fetches recent news via Google News RSS (India-focused for your Bengaluru location),
# sends the raw list to Grok (xAI API) for intelligent filtering/summarization to the
# top 20 most relevant items based on YOUR area of interest,
# then generates a clean, self-contained HTML file with today's date & time.
#
# Requirements (run once):
#   pip install openai feedparser
#
# Usage:
#   export XAI_API_KEY=your_actual_key_here
#   python get_news.py --interest "artificial intelligence and machine learning"
#
# The script will create a file like: news_2026-04-16_11-35.html
# Open it in any browser — no internet required after generation.
# ================================================

import os
import json
import argparse
from datetime import datetime
import feedparser
from openai import OpenAI

# ------------------- CONFIG -------------------
RSS_URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"  # India top headlines (change if you want global)
MAX_RAW_NEWS = 60          # How many raw items to fetch before sending to Grok
MODEL = "grok-4.20-non-reasoning"   # Fast & cost-effective Grok model (change to "grok-4.20-reasoning" if you want deeper analysis)

# ------------------- ARGUMENTS -------------------
parser = argparse.ArgumentParser(description="Get personalized top 20 news using Grok API")
parser.add_argument("--interest", type=str, required=True,
                    help="Your area of interest (e.g. 'AI and technology', 'Indian startups', 'climate change', etc.)")
args = parser.parse_args()

INTEREST = args.interest.strip()

# ------------------- FETCH RAW NEWS (Web data) -------------------
print("Fetching latest news from Google News (India)...")
feed = feedparser.parse(RSS_URL)

raw_news = []
for entry in feed.entries[:MAX_RAW_NEWS]:
    raw_news.append({
        "title": entry.title,
        "link": entry.link,
        "summary": entry.get("summary", "")[:300],   # truncate long summaries
        "published": entry.get("published", "")
    })

print(f"✅ Fetched {len(raw_news)} raw news items.")

if not raw_news:
    print("No news fetched. Check your internet.")
    exit(1)

# ------------------- PREPARE PROMPT FOR GROK -------------------
news_list_str = "\n\n".join([
    f"Title: {item['title']}\nLink: {item['link']}\nSummary: {item['summary']}\nPublished: {item['published']}"
    for item in raw_news
])

system_prompt = """You are an expert news curator.
Given a list of recent news items and a user's specific area of interest, 
select the TOP 20 most relevant news items.
For each selected item:
- Keep the original title and link
- Write a short, engaging 1-2 sentence summary
- Add a one-sentence "Why relevant" explanation

Return ONLY valid JSON in this exact format (no extra text, no markdown):
{
  "news": [
    {
      "title": "...",
      "link": "...",
      "summary": "...",
      "why_relevant": "..."
    },
    ...
  ]
}
"""

user_prompt = f"""User's area of interest: {INTEREST}

Here are the recent news items:

{news_list_str}
"""

print("Sending to Grok for intelligent filtering...")

# ------------------- CALL GROK API -------------------
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ],
    temperature=0.3,      # fairly deterministic for curation
    max_tokens=8000,
    response_format={"type": "json_object"}   # forces JSON output
)

# Parse Grok's JSON response
try:
    result = json.loads(response.choices[0].message.content)
    filtered_news = result["news"][:20]   # safety limit
except Exception as e:
    print("Error parsing Grok response:", e)
    print("Raw response:", response.choices[0].message.content)
    exit(1)

print(f"✅ Grok filtered to {len(filtered_news)} relevant news items.")

# ------------------- GENERATE HTML FILE -------------------
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M")
filename = f"news_{date_str}_{now.strftime('%H-%M')}.html"
timestamp = now.strftime("%A, %B %d, %Y %I:%M %p IST")

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top 20 News • {INTEREST} • {date_str}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
        body {{ font-family: 'Inter', system-ui, sans-serif; margin: 0; padding: 20px; background: #0f0f0f; color: #fff; line-height: 1.6; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        h1 {{ text-align: center; margin-bottom: 10px; color: #00ff9d; }}
        .subtitle {{ text-align: center; color: #aaa; margin-bottom: 30px; }}
        .news-card {{ background: #1a1a1a; border-radius: 12px; padding: 20px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); transition: transform 0.2s; }}
        .news-card:hover {{ transform: translateY(-3px); }}
        .title {{ font-size: 1.3rem; font-weight: 600; margin: 0 0 10px 0; color: #00ff9d; }}
        .summary {{ color: #ddd; margin: 12px 0; }}
        .why {{ font-size: 0.95rem; color: #00cc77; font-style: italic; }}
        .meta {{ color: #888; font-size: 0.9rem; display: flex; justify-content: space-between; align-items: center; }}
        a {{ color: #00ff9d; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .footer {{ text-align: center; margin-top: 50px; color: #555; font-size: 0.9rem; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔥 Your Top 20 News</h1>
        <p class="subtitle">Personalized for: <strong>{INTEREST}</strong><br>
        Generated on {timestamp} using Grok (xAI)</p>
        
        {''.join(f'''
        <div class="news-card">
            <h2 class="title"><a href="{item['link']}" target="_blank">{item['title']}</a></h2>
            <p class="summary">{item['summary']}</p>
            <p class="why">✅ Why relevant: {item['why_relevant']}</p>
            <div class="meta">
                <span><a href="{item['link']}" target="_blank">Read full story →</a></span>
            </div>
        </div>
        ''' for item in filtered_news)}
        
        <div class="footer">
            Powered by Grok API • Data from Google News • 
            {len(filtered_news)} stories • {timestamp}
        </div>
    </div>
</body>
</html>
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"\n🎉 Done! HTML file generated: {filename}")
print("   Open it in your browser to view your personalized news.")
