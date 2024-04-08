"""
Django settings for aquaevitae_api project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import json

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", True)

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(" ")

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(" ")

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(" ")
CORS_ALLOW_ALL_ORIGINS = os.getenv("CORS_ALLOW_ALL_ORIGINS", False)

# Config Dev Dotenv
from dotenv import load_dotenv

if DEBUG:
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# Actual directory user files go to
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "mediafiles")

# URL used to access the media
MEDIA_URL = "/images/"

ARTIFACTS_URL = os.path.join(os.path.dirname(BASE_DIR), "artifacts")

# Application definition
EXTERNAL_APPS = [
    "phonenumber_field",
    "drf_yasg",
    "rest_framework",
    "django_admin_multiple_choice_list_filter",
    'django_filters',
    "corsheaders",
]

INTERNAL_APPS = [
    "companies",
    "partnerships",
    "products",
    "recommendations",
    "analysis",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = DJANGO_APPS + INTERNAL_APPS + EXTERNAL_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "aquaevitae_api.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "aquaevitae_api.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_USER_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend', "rest_framework.filters.SearchFilter", "rest_framework.filters.OrderingFilter"],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Application settings
SKIN_TYPE_MAX_NUMBER = os.getenv("SKIN_TYPE_MAX_NUMBER", 3)
SKIN_DISEASE_MAX_NUMBER = os.getenv("SKIN_DISEASE_MAX_NUMBER", 5)
REQUEST_TIME_LIMIT = os.getenv("REQUEST_TIME_LIMIT", 90)  # Days
ANALYSIS_STORAGE_FOLDER = os.path.join(BASE_DIR, "analysis", "images")
ML_MODELS_PATH = os.path.join(ARTIFACTS_URL, "models")
MP_LANDMARK_MODEL = os.getenv("MP_LANDMARK_MODEL", "face_landmarker.task")
WRINKLES_MODEL = os.getenv("WRINKLES_MODEL", "sgd_lr001_tunning8_norotation_eliptic_white.keras")
MAX_AGE_DIFFERENCE = os.getenv("MAX_AGE_DIFFERENCE", 10)

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "guilhermetonello@ipb.pt")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_USE_TLS=os.getenv("EMAIL_USE_TLS", True)

CELERY_broker_url = os.getenv("CELERY_BROKER_URL")
accept_content = json.loads(os.getenv("CELERY_ACCEPT_CONTENT"))
result_serializer = os.getenv("CELERY_RESULT_SERIALIZER")
task_serializer = os.getenv("CELERY_TASK_SERIALIZER")
result_backend = os.getenv("CELERY_RESULT_BACKEND")
