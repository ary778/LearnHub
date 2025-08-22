import os
import requests
from django.conf import settings

YOUTUBE_API_KEY = getattr(settings, 'YOUTUBE_API_KEY', os.getenv('YOUTUBE_API_KEY', ''))
GOOGLE_BOOKS_API_KEY = getattr(settings, 'GOOGLE_BOOKS_API_KEY', os.getenv('GOOGLE_BOOKS_API_KEY', ''))

# -------- Google Books --------
def fetch_google_books(query: str, max_results: int = 5):
    params = {'q': query, 'maxResults': max_results, 'printType': 'books'}
    if GOOGLE_BOOKS_API_KEY:
        params['key'] = GOOGLE_BOOKS_API_KEY
    r = requests.get('https://www.googleapis.com/books/v1/volumes', params=params, timeout=20)
    r.raise_for_status()
    items = r.json().get('items', [])
    results = []
    for it in items:
        info = it.get('volumeInfo', {})
        results.append({
            'title': info.get('title'),
            'authors': info.get('authors', []),
            'publisher': info.get('publisher'),
            'publishedDate': info.get('publishedDate'),
            'thumbnail': (info.get('imageLinks') or {}).get('thumbnail'),
            'url': info.get('infoLink') or info.get('previewLink'),
        })
    return results

# -------- YouTube --------
def fetch_youtube_videos(query: str, max_results: int = 6):
    if not YOUTUBE_API_KEY:
        return []
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': max_results,
        'key': YOUTUBE_API_KEY,
        'safeSearch': 'none',
    }
    r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params, timeout=20)
    r.raise_for_status()
    data = r.json().get('items', [])
    out = []
    for it in data:
        video_id = it['id']['videoId']
        sn = it['snippet']
        out.append({
            'title': sn.get('title'),
            'channel': sn.get('channelTitle'),
            'publishedAt': sn.get('publishedAt'),
            'thumbnail': (sn.get('thumbnails') or {}).get('high', {}).get('url'),
            'url': f'https://www.youtube.com/watch?v={video_id}',
        })
    return out

# -------- Codeforces Problems --------
def fetch_codeforces_problems(query: str, max_results: int = 20):
    r = requests.get('https://codeforces.com/api/problemset.problems', timeout=30)
    r.raise_for_status()
    payload = r.json()
    if payload.get('status') != 'OK':
        return []
    problems = payload.get('result', {}).get('problems', [])
    q = query.lower()
    filtered = []
    for p in problems:
        name = p.get('name', '')
        tags = p.get('tags', [])
        if q in name.lower() or any(q in t.lower() for t in tags):
            cid = p.get('contestId')
            idx = p.get('index')
            url = f'https://codeforces.com/problemset/problem/{cid}/{idx}' if cid and idx else 'https://codeforces.com/problemset'
            filtered.append({'title': name, 'tags': tags, 'rating': p.get('rating'), 'url': url})
            if len(filtered) >= max_results:
                break
    return filtered

# -------- Codeforces Blogs (filter recent entries) --------
def fetch_codeforces_blogs(query: str, max_actions: int = 200):
    r = requests.get('https://codeforces.com/api/recentActions', params={'maxCount': max_actions}, timeout=20)
    r.raise_for_status()
    payload = r.json()
    if payload.get('status') != 'OK':
        return []
    actions = payload.get('result', [])
    q = query.lower()
    results = []
    for act in actions:
        blog = (act.get('blogEntry') or {})
        title = blog.get('title')
        if not title:
            continue
        if q in title.lower():
            bid = blog.get('id')
            results.append({
                'title': title,
                'authorHandle': (blog.get('author') or {}).get('handle'),
                'creationTimeSeconds': blog.get('creationTimeSeconds'),
                'url': f'https://codeforces.com/blog/entry/{bid}' if bid else 'https://codeforces.com/blog',
            })
    return results[:10]
