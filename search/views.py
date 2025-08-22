# search/views.py

from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache
import requests
from googleapiclient.discovery import build
from rest_framework.decorators import api_view
from rest_framework.response import Response

def home(request):
    """Renders the home page with the search form."""
    return render(request, 'search/home.html')

def search_results(request):
    """
    Checks cache or fetches results from APIs and renders them in a template.
    """
    query = request.GET.get('q', '').strip()
    context = {'query': query}

    if not query:
        return render(request, 'search/results.html', context)

    cache_key = f'search_results_{query.lower()}'
    cached_results = cache.get(cache_key)

    if cached_results:
        print(f"Serving results for '{query}' from CACHE.")
        context.update(cached_results)
    else:
        print(f"Fetching results for '{query}' from APIs.")
        youtube_results = search_youtube(query)
        books_results = search_google_books(query)
        codeforces_problems = search_codeforces(query)
        codeforces_blogs = search_codeforces_blogs(query)

        api_results = {
            'youtube_results': youtube_results,
            'books_results': books_results,
            'codeforces_results': codeforces_problems,
            'codeforces_blogs': codeforces_blogs,
        }
        
        cache.set(cache_key, api_results, 3600) # Cache for 1 hour
        context.update(api_results)
        
    return render(request, 'search/results.html', context)

@api_view(['GET'])
def search_api(request):
    """
    API endpoint that returns search results as JSON.
    """
    query = request.GET.get('q', '').strip()
    
    if not query:
        return Response({'error': 'A search query "q" is required.'}, status=400)

    cache_key = f'search_api_{query.lower()}'
    cached_results = cache.get(cache_key)

    if cached_results:
        print(f"Serving API results for '{query}' from CACHE.")
        return Response(cached_results)
    
    print(f"Fetching API results for '{query}' from APIs.")
    results = {
        'youtube': search_youtube(query),
        'books': search_google_books(query),
        'codeforces_problems': search_codeforces(query),
        'codeforces_blogs': search_codeforces_blogs(query),
    }

    cache.set(cache_key, results, 3600)
    return Response(results)

# --- HELPER FUNCTIONS ---

def search_youtube(query):
    try:
        youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
        search_response = youtube.search().list(q=query, part='snippet', maxResults=5, type='video').execute()
        results = []
        for item in search_response.get('items', []):
            results.append({
                'title': item['snippet']['title'],
                'video_id': item['id']['videoId'],
                'thumbnail': item['snippet']['thumbnails']['default']['url'],
            })
        return results
    except Exception as e:
        print(f"An error occurred with YouTube API: {e}")
        return []

def search_google_books(query):
    try:
        url = "https://www.googleapis.com/books/v1/volumes"
        params = {'q': query, 'key': settings.GOOGLE_BOOKS_API_KEY, 'maxResults': 5}
        response = requests.get(url, params=params)
        response.raise_for_status()
        results = []
        for item in response.json().get('items', []):
            volume_info = item.get('volumeInfo', {})
            results.append({
                'title': volume_info.get('title', 'No Title'),
                'authors': volume_info.get('authors', ['Unknown Author']),
                'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail'),
                'info_link': volume_info.get('infoLink')
            })
        return results
    except Exception as e:
        print(f"An error occurred with Google Books API: {e}")
        return []

def search_codeforces(query):
    try:
        url = f"https://codeforces.com/api/problemset.problems?tags={query}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['status'] == 'OK':
            results = []
            for problem in data['result']['problems'][:5]:
                results.append({
                    'name': problem['name'],
                    'rating': problem.get('rating', 'N/A'),
                    'link': f"https://codeforces.com/problemset/problem/{problem.get('contestId')}/{problem.get('index')}"
                })
            return results
        return []
    except Exception as e:
        print(f"An error occurred with Codeforces API: {e}")
        return []

def search_codeforces_blogs(query):
    handles = ["Errichto", "Petr", "SecondThread"]
    all_matching_blogs = []
    for handle in handles:
        try:
            url = f"https://codeforces.com/api/user.blogEntries?handle={handle}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data['status'] == 'OK':
                for blog in data['result']:
                    if query.lower() in blog['title'].lower():
                        all_matching_blogs.append({
                            'title': blog['title'],
                            'author': blog['authorHandle'],
                            'link': f"https://codeforces.com/blog/entry/{blog['id']}"
                        })
        except Exception as e:
            print(f"An error occurred fetching blogs for {handle}: {e}")
            continue
    return all_matching_blogs[:5]