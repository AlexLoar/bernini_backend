# encoding: utf-8

from datetime import datetime
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# PATH CONFIGURATION
# ------------------------------------------------------------------------------
# Path to the django repo directory:
ROOT_DIR = dirname(dirname(dirname(dirname(abspath(__file__)))))

# Path to the project directory:
APPS_DIR = dirname(dirname(dirname(abspath(__file__))))

# Absolute filesystem path to the config directory:
CONFIG_ROOT = normpath(join(APPS_DIR, 'config'))

# Absolute filesystem path to the project directory:
PROJECT_ROOT = str(APPS_DIR)

# Absolute filesystem path to the django repo directory:
DJANGO_ROOT = str(ROOT_DIR)

# Project folder:
PROJECT_FOLDER = basename(PROJECT_ROOT)

# Project name:
PROJECT_NAME = basename(PROJECT_ROOT).capitalize()

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(CONFIG_ROOT)


# DEBUG CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#debug
DEBUG = True


# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#admins
ADMINS = (
    ('Alex Lopez', 'alopezariguel@gmail.com.com'),
)

# See: https://docs.djangoproject.com/en/1.8/ref/settings/#managers
MANAGERS = ADMINS

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.8/ref/settings/#time-zone
TIME_ZONE = 'UTC'

# https://docs.djangoproject.com/en/1.8/ref/settings/#language-code
LANGUAGE_CODE = 'es-es'

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#use-tz
USE_TZ = True


# APP CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.8/ref/settings/#installed-apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
)

THIRD_PARTY_APPS = (
    'grappelli',
    'rest_framework',
)

PROJECT_APPS = (
    'orders',
)

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + PROJECT_APPS


# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.8/ref/settings/#static-root
STATIC_ROOT = APPS_DIR + "/"

# https://docs.djangoproject.com/en/1.8/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    normpath(join(APPS_DIR, 'static/')),
)

# https://docs.djangoproject.com/en/1.8/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
]


# URL CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/1.8/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'


# LOGGING CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.8/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
      'production_only': {
          '()': 'django.utils.log.RequireDebugFalse'
      }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s'
        },
        'messageonly': {
            'format': '%(message)s'
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '{}/django-{}.log'.format(APPS_DIR, datetime.now().strftime('%Y%m%d')),
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
            },
    },
    'loggers': {
        'orders': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True
        }
    },
}


ALLOWED_HOSTS = ['*']

# TEMPLATES CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.8/ref/templates/
TEMPLATE_DIRS = (
    normpath(join(APPS_DIR, 'templates')),
)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
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


# SECRETS CONFIGURATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/1.8/ref/settings/#secret-key
SECRET_KEY = 'bl28wrk@2ss9iq&*am-fd!j8b6ic*rxl0ua$j5^cuz#8o344_^'
