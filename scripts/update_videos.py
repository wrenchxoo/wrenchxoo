"""Refresh latest public videos from WRENCHXOO's YouTube Atom feed.
No API key required. Safe failure: do not overwrite existing videos.json.
"""
import json
import pathlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHANNEL = "https://www.youtube.com/@wrenchxoo"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; WrenchxooFeedBot/1.0)"}


def get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=25) as response:
        return response.read().decode("utf-8")


def run():
    html = get(CHANNEL)
    match = re.search(r'"channelId"\s*:\s*"(UC[A-Za-z0-9_-]+)"', html)
    if not match:
        match = re.search(r'"externalId"\s*:\s*"(UC[A-Za-z0-9_-]+)"', html)
    if not match:
        match = re.search(r'https://www\.youtube\.com/feeds/videos\.xml\?channel_id=(UC[A-Za-z0-9_-]+)', html)
    if not match:
        raise RuntimeError("Could not resolve YouTube channel ID; existing data is unchanged")
    channel_id = match.group(1)
    xml = get("https://www.youtube.com/feeds/videos.xml?channel_id=" + channel_id)
    root = ET.fromstring(xml)
    ns = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}
    videos = []
    for entry in root.findall("a:entry", ns):
        id = entry.findtext("yt:videoId", default="", namespaces=ns)
        if not re.fullmatch(r"[A-Za-z0-9_-]{11}", id):
            continue
        videos.append({"id": id, "title": entry.findtext("a:title", default="WRENCHXOO", namespaces=ns), "published": entry.findtext("a:published", default="", namespaces=ns)})
    if not videos:
        raise RuntimeError("Feed returned no videos; existing data is unchanged")
    path = ROOT / "data" / "videos.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"videos": videos[:9]}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Saved {len(videos[:9])} videos from channel {channel_id}")


if __name__ == "__main__":
    try:
        run()
    except Exception as exc:
        print(f"Refresh unavailable: {exc}", file=sys.stderr)
        sys.exit(1)
