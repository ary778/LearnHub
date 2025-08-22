# search/urls.py

from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.search_results, name='search_results'),
    
    # This is the new line for your API endpoint
    path('api/search/', views.search_api, name='search_api'),
]