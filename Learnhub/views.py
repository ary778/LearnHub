# Learnhub/views.py

from django.shortcuts import redirect

def index(request):
    """
    Redirects the project's root URL to the search app's home page.
    """
    return redirect('search:home')