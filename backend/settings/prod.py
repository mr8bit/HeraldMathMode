from backend.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_NAME', 'None'),
        'USER': os.getenv('POSTGRES_USER', 'None'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'None'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', 'localhost'),
    }
}

ALLOWED_HOSTS = ['*', ]

WEBHOOK_SITE = os.getenv('WEBHOOK_SITE', 'None')

VIBER_BOT = {
    "VIBER_BOT_NAME": os.getenv('VIBER_BOT_NAME', 'EventDevBot'),
    "VIBER_AUTH_TOKEN": os.getenv('VIBER_AUTH_TOKEN', 'None'),
    "VIBER_AVATAR": os.getenv('VIBER_AVATAR', 'https://www.viber.com/avatar.jpg'),
    'WEBHOOK_SITE': WEBHOOK_SITE,
    'WEBHOOK_PREFIX': '/viber',  # (Optional[str]) # If this value is specified,
}

DJANGO_TELEGRAMBOT = {
    'MODE': 'WEBHOOK',  # (Optional [str]) # The default value is WEBHOOK,
    'WEBHOOK_SITE': WEBHOOK_SITE,
    'WEBHOOK_PREFIX': '/bot',  # (Optional[str]) # If this value is specified,
    'BOTS': [
        {
            'TOKEN': os.getenv('TELEGRAM_TOKEN', 'None'),  # Your bot token.
        },
    ],

}

## SENTRY

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_dist"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


RAVEN_CONFIG = {
    'dsn': os.getenv('SENTRY'),
}

INSTALLED_APPS = INSTALLED_APPS + [  # NOQA (ignore all errors on this line)
    'raven.contrib.django.raven_compat',
]

# ####### Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['sentry'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['sentry'],
            'propagate': False,
        },
    },
}

DEFAULT_LOGGER = 'raven'

LOGGER_EXCEPTION = DEFAULT_LOGGER
LOGGER_ERROR = DEFAULT_LOGGER
LOGGER_WARNING = DEFAULT_LOGGER
