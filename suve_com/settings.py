import os
from pathlib import Path
import environ

from rest_framework.settings import api_settings # импорт настроек для DRF
from django.conf.global_settings import SERVER_EMAIL


BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env() # Инициализация переменных окружения
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))# Загрузка переменные окружения из файла .env
SECRET_KEY = env('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

INTERNAL_IPS = [
    "127.0.0.1",
]


INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'suve_main.apps.SuveMainConfig',
    'suve_auth.apps.SuveAuthConfig',
    'ws_app.apps.WsAppConfig',
    'debug_toolbar',
    'channels',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'suve_com.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'suve_com/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'suve_com.context_processors.get_menu_context',
            ],
        },
    },
]

# WSGI_APPLICATION = 'suve_com.wsgi.application'
ASGI_APPLICATION = 'suve_com.asgi.application'

# подключение postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432'
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

AUTHENTICATION_BACKENDS = ['suve_auth.authentication.EmailAuthBackend', # подключение собстевнного backend
                           'django.contrib.auth.backends.ModelBackend' # backend по умолчанию
                           ]
#настройка backend google для отправки по протоколу smtp
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Настройка загрузки статических файлов
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    './suve_com/static'
]

MEDIA_ROOT = './media/'
MEDIA_URL = '/media/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATA_UPLOAD_MAX_NUMBER_FIELDS = 5000


LOGIN_REDIRECT_URL = 'main' # настройка redirect после login
LOGOUT_REDIRECT_URL = 'main' # настройка redirect после logout
LOGIN_URL = 'auth:login' # настройка redirect для неавторизованных пользователей

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated', # настройка permissions для DRF
    ]
}


