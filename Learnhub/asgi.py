"""
ASGI config for LearnHub_Final_Full project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearnHub_Final_Full.settings')

application = get_asgi_application()
