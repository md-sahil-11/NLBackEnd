from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ALLOWED_ORIGINS = [
    "https://nl-frontend-seven.vercel.app",
    "http://sahil11.pythonanywhere.com",
]

ALLOWED_HOSTS = [
    "sahil11.pythonanywhere.com",
    "nl-frontend-seven.vercel.app"
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

CORS_ORIGIN_WHITELIST = (
    "https://nl-frontend-seven.vercel.app",
    "http://sahil11.pythonanywhere.com",
)
