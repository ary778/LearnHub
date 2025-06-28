import time
import requests
from bs4 import BeautifulSoup, Tag
from urllib.parse import unquote
from django.conf import settings
from typing import List, Dict
from serpapi import GoogleSearch

YOUTUBE_API_KEY = getattr(settings, 'YOUTUBE_API_KEY', '')
SERP_API_KEY = "d6270772107d49bfe9ee0a7f41af9de96999448b62b109efc053dc49aeaf883a"

def get_youtube_results(query: str, max_results: int = 5) -> List[Dict]:
    if not YOUTUBE_API_KEY:
        print("YouTube API key not configured")
        return []

    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "key": YOUTUBE_API_KEY,
        "maxResults": max_results,
        "type": "video",
        "relevanceLanguage": "en"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return parse_youtube_response(response.json(), max_results)
    except requests.RequestException as e:
        print(f"YouTube API request failed: {str(e)}")
        return []

def parse_youtube_response(data: Dict, max_results: int) -> List[Dict]:
    results = []
    for item in data.get("items", [])[:max_results]:
        try:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            results.append({
                "title": title,
                "url": f"https://youtube.com/watch?v={video_id}",
                "thumbnail": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
            })
        except (KeyError, TypeError) as e:
            print(f"Error parsing YouTube result: {str(e)}")
    return results

def get_codeforces_links(topic: str) -> List[Dict]:
    tag = topic.lower().replace(" ", "-")
    return [{
        "title": f"Codeforces problems tagged '{topic}'",
        "url": f"https://codeforces.com/problemset?tags={tag}"
    }]

def get_search_links(topic: str, source: str) -> List[Dict]:
    if not topic.strip():
        return []

    query = topic.replace(" ", "+")
    links = []

    if source in ['gfg', 'all']:
        links += get_serpapi_links(query, "geeksforgeeks.org")
    if source in ['medium', 'all']:
        links += get_serpapi_links(query, "medium.com")

    return links[:3]

def get_serpapi_links(query: str, site: str) -> List[Dict]:
    if not query or not site:
        return []

    try:
        search = GoogleSearch({
            "q": f"site:{site} {query}",
            "api_key": SERP_API_KEY
        })
        results = search.get_dict().get("organic_results", [])
        final_links = []

        for r in results:
            if site in r.get("link", ""):
                final_links.append({
                    "title": r.get("title", "Untitled"),
                    "url": r.get("link")
                })

        return final_links[:3]
    except Exception as e:
        print(f"SerpAPI error for {site}: {str(e)}")
        return []
