from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('search.urls')),  # this includes your app
    path('admin/', admin.site.urls),
]
