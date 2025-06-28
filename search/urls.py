from django.urls import path
from . import views
# Add this for namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
]