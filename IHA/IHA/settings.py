from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ezbb$t3w&k4=b+93m-3uep*og@%(y1uuoy$q+4mq6kuhzj&qj#'

DEBUG = True

ALLOWED_HOSTS = ["*"] # change this to your domain name

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # My apps
    'iha_app.apps.IhaAppConfig',
    'iha_api.apps.IhaApiConfig',
    'user_app.apps.UserAppConfig',
    # Third party apps
    'rest_framework',    # REST API
    'django_extensions', # Django extensions
    'django_filters',    # Django filters
    #'debug_toolbar',    # Django debug toolbar (only for development)
    'crispy_forms',      # Django crispy forms (Bootstrap4)
    'rest_auth',         # Django rest auth api for login and logout
    'mptt',              # Django mptt for tree structure

]

MIDDLEWARE = [
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IHA.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'IHA.wsgi.application'


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'baykar',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        #'HOST': 'localhost',
        'HOST': 'db', # for docker
        'PORT': '5432',
    }
}

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# Django rest framework settings
"""
API settings 
    - AUTHENTICATION settings
    - PERMISSION settings
    - PAGINATION settings
"""
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
}

# Internationalization

LOCALE_PATHS = [
    os.path.join(BASE_DIR,"locale")
]

LANGUAGES = (
    ('tr',_('Turkish')),
    ('en',_('English')),
)


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Istanbul'

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Crispy forms settings (Bootstrap4)
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
# Django message taglara error ekldik
MESSAGE_TAGS = {
    messages.ERROR:'danger'
}

PAGINATION_NUMBER = 25

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
