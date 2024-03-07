import os
from decouple import config,Csv
from django.contrib.messages import constants
from pathlib import Path

DATE_FORMAT = "d-m-Y"


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY =config('SECRET_KEY')

DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    "127.0.0.1",
    "https://mundocoloridokids.com.br/",
    "http://154.49.246.53/"
]


INSTALLED_APPS = [
    'clearcache',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'ckeditor',
    'Core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'News.urls'

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

WSGI_APPLICATION = 'News.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

LANGUAGES = (
    ('pt', u'Português'),
    ('en', u'Inglês'),
)

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL='/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}

DEFAULT_FROM_EMAIL=config('EMAIL_HOST_USER')
EMAIL_BACKEND ='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER= config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD= config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS=True
EMAIL_PORT =587
EMAIL_HOST='smtp.office365.com'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SESSION_COOKIE_AGE = 86400 # 24 horas * 60 minutos * 60 segundos

SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = os.path.join(BASE_DIR,'tmp/')


CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-3.6.0.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['Link', 'Unlink'],
            ['NumberedList', 'BulletedList'],
            ['Image', 'Table'],
            ['Format', 'RemoveFormat'],
            ['Source'],
        ],
        'width': 800,
        'height': 300,
        'tabSpaces': 4,
    },
}


LOGGING = {
    'version': 1,
    # The version number of our log
    'disable_existing_loggers': False,
    # django uses some of its own loggers for internal operations. In case you want to disable them just replace the False above with true.
    # A handler for WARNING. It is basically writing the WARNING messages into a file called WARNING.log
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'warning.log',
        },
		'file1': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'INFO.log',
        },
		'file2': {
            'level': 'CRITICAL',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'Critical.log',
        },
    },
    # A logger for WARNING which has a handler called 'file'. A logger can have multiple handler
    'loggers': {
       # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        '': {
            'handlers': ['file'], #notice how file variable is called in handler which has been defined above
            'level': 'WARNING',
            'propagate': True,
        },
    },
	'loggers': {
       # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        '': {
            'handlers': ['file1'], #notice how file variable is called in handler which has been defined above
            'level': 'INFO',
            'propagate': True,
        },
    },
    'loggers': {
       # notice the blank '', Usually you would put built in loggers like django or root here based on your needs
        '': {
            'handlers': ['file2'], #notice how file variable is called in handler which has been defined above
            'level': 'CRITICAL',
            'propagate': True,
        },
    },
}