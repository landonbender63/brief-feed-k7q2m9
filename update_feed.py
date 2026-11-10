"""Write feed.json for the Alexa Flash Briefing.

Usage: python3 update_feed.py brief.txt
brief.txt holds the plain spoken text Alexa should read (max 4500 characters).
"""
import json
import sys
import uuid
from datetime import datetime, timezone

MAX_CHARS = 4500

text = open(sys.argv[1], encoding="utf-8").read().strip()
text = " ".join(text.split())  # one paragraph, no stray newlines
if len(text) > MAX_CHARS:
    text = text[: MAX_CHARS - 3].rsplit(" ", 1)[0] + "..."

now = datetime.now(timezone.utc)
feed = {
    "uid": f"urn:uuid:{uuid.uuid4()}",
    "updateDate": now.strftime("%Y-%m-%dT%H:%M:%S.0Z"),
    "titleText": "Landon's morning brief",
    "mainText": text,
    "redirectionUrl": "https://claude.ai",
}

with open("feed.json", "w", encoding="utf-8") as f:
    json.dump(feed, f, ensure_ascii=False, indent=2)
print(f"feed.json written, {len(text)} characters, {feed['updateDate']}")
