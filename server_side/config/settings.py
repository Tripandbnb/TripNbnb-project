"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "hi^du)n!jw(8-ihbjacbn-eu@*p0h^c24**hi%09r7-r!vu#u&"
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "hi^du)n!jw(8-ihbjacbn-eu@*p0h^c24**hi%09r7-r!vu#u&")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )

ALLOWED_HOSTS = ['*', 'https://tripnbnbserver.herokuapp.com/']


# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = ["corsheaders", "rest_framework", "django_seed",]

PROJECT_APPS = [
    "core.apps.CoreConfig",
    "users.apps.UsersConfig",
    "places.apps.PlacesConfig",
    "reviews.apps.ReviewsConfig",
    "lists.apps.ListsConfig",
    "reservations.apps.ReservationsConfig",
] + THIRD_PARTY_APPS


INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
"default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

db_from_env = dj_database_url.config(conn_max_age=500) 
DATABASES['default'].update(db_from_env)
django_heroku.settings(locals())


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

AUTH_USER_MODEL = "users.User"

<<<<<<< HEAD
CORS_ORIGIN_WHITELIST = ["https://localhost:3000", 'https://tripbnb.netlify.app']
=======
CORS_ORIGIN_WHITELIST = ["https://localhost:3000", "https://tripbnb.netlify.app/"]
>>>>>>> 1c8e7943d808c6f76a83db8ed6b52dc3767287d4

MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

MEDIA_URL = "/media/"
