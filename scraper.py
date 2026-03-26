import warnings
import requests
import re
from bs4 import XMLParsedAsHTMLWarning, BeautifulSoup

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

keywords = [
    "earthquake", "flood", "cyclone", "tsunami",
    "wildfire", "drought", "famine",
    "war", "conflict", "refugee",
    "displacement", "humanitarian crisis"
]

blocked_words = [
    "report", "outlook", "update", "watch",
    "planning", "situation","capacity", "strengthening"
]

rss_feeds = {
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "CNN": "https://www.aljazeera.com/xml/rss/all.xml",
    "ReliefWeb": "https://reliefweb.int/updates/rss.xml",
    "Guardian": "https://www.theguardian.com/world/rss",
    "USGS": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.atom"
}

def fetch_disaster_news():
    headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
    results = {}

    for source, url in rss_feeds.items():
        headlines = []
        res = requests.get(url, timeout=10,headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.find_all("item")

        printed = set()

        for item in items:
            title_tag = item.find("title")
            if not title_tag:
                continue

            title = title_tag.text.strip()
            title_lower = title.lower()

            if any(bad in title_lower for bad in blocked_words):
                continue

            for key in keywords:
                pattern = r"\b" + re.escape(key) + r"\b"
                if re.search(pattern, title_lower):
                    if title not in printed:
                        headlines.append(title)
                        printed.add(title)
                    break

        results[source] = headlines

    return results
