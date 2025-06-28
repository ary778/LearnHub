from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .utils import get_youtube_results, get_codeforces_links, get_search_links

@require_http_methods(["GET"])
def home(request):
    """Render search form"""
    return render(request, 'search/form.html')

@require_http_methods(["POST"])
def results(request):
    """Handle search and render results"""
    try:
        topic = request.POST.get('topic', '').strip()
        if not topic:
            return render(request, 'search/form.html', {
                'error': 'Please enter a search topic'
            })

        source = request.POST.get('source', 'all').strip().lower()

        context = {
            'topic': topic,
            'youtube_results': get_youtube_results(topic) if source in ['youtube', 'all'] else [],
            'codeforces_links': get_codeforces_links(topic) if source in ['codeforces', 'all'] else [],
            'google_links': get_search_links(topic, source) if source in ['gfg', 'medium', 'all'] else [],
        }

        print(f"Search results for '{topic}':", {
            'youtube': len(context['youtube_results']),
            'codeforces': len(context['codeforces_links']),
            'articles': len(context['google_links'])
        })

        return render(request, 'search/results.html', context)

    except Exception as e:
        print("Search error:", str(e))
        return render(request, 'search/form.html', {
            'error': 'An error occurred. Please try again.'
        })
