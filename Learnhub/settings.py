# Learnhub/settings.py (partial - replace relevant parts)
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Load .env
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')  # fallback only for dev
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # default apps...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # your apps
    'search',
    'accounts',
]

# ... middleware, templates ...
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],   # ✅ tells Django where templates folder is
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# PostgreSQL from env
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'learnhub',      # database name you just created
        'USER': 'postgres',      # your pgAdmin username
        'PASSWORD': '1234',  # your pgAdmin password
        'HOST': 'localhost',     # or 127.0.0.1
        'PORT': '5432',          # default PostgreSQL port
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
# Auth redirects
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# API keys
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', '')
GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY', '')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Where collected static files will be stored (for production)
STATIC_ROOT = BASE_DIR / "staticfiles"

# Additional directories where Django will look for static files
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media files (user uploads, e.g. profile pictures)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

ROOT_URLCONF = 'Learnhub.urls'
