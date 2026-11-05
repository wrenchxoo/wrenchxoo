#!/usr/bin/env python3
"""Fetch public YouTube channel stats via official Data API v3; never print the key."""
import datetime as dt
import json
import os
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

key = os.environ.get("YOUTUBE_API_KEY", "").strip()
if not key:
    raise SystemExit("Missing YOUTUBE_API_KEY GitHub Actions secret")

params = urlencode({"part": "statistics,snippet", "forHandle": "wrenchxoo", "key": key})
request = Request("https://www.googleapis.com/youtube/v3/channels?" + params,
                  headers={"User-Agent": "WrenchxooGitHubPagesStats/1.0"})
try:
    with urlopen(request, timeout=25) as response:
        payload = json.load(response)
except (HTTPError, URLError) as exc:
    raise SystemExit("Could not fetch YouTube statistics; check API key and quota") from exc
items = payload.get("items") or []
if len(items) != 1:
    raise SystemExit("The channel @wrenchxoo was not found")
channel = items[0]
stats = channel.get("statistics", {})
hidden = stats.get("hiddenSubscriberCount", False)
count = None if hidden else stats.get("subscriberCount")
if not hidden and (count is None or not str(count).isdigit()):
    raise SystemExit("API response has no subscriberCount")
result = {
    "channel": "wrenchxoo",
    "channel_id": channel["id"],
    "hidden_subscriber_count": bool(hidden),
    "subscriber_count": None if hidden else int(count),
    "video_count": int(stats.get("videoCount", 0)),
    "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
}
path = Path("data/channel-stats.json")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("YouTube channel statistics updated successfully")
