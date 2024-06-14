"""
Django settings for TallerRayoMakween project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$3ndiow*$spzlciv@+(x+s(91#yu+2)0ms8y!om(5ckzphd23m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#Para probar la pagina 404
#DEBUG = False

#ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'admin_confirm',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'crispy_forms',
    'crispy_bootstrap4',
    'rest_framework',
    'axes',
    'captcha',
    'django_recaptcha',
]

X_FRAME_OPTIONS = "SAMEORIGIN"
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# RECAPTCHA
RECAPTCHA_PUBLIC_KEY = '6LekLfcpAAAAAPkRH764CYWWw5od-gMh6CMZhokV'
RECAPTCHA_PRIVATE_KEY = '6LekLfcpAAAAAIbZewBfjrqKtcAo2iwqD4ENnbD7'

# CONFIG AXES

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

AXES_FAILURE_LIMIT = 3 # SON LOS NUMEROS DE INTENTOS FALLIDOS POR EL USUARIO
AXES_COOLOFF_TIME = timedelta(minutes=1) # CANTIDAD DE TIEMPO QUE TIENE QUE ESPERAR ANTES DE OTRO LOG
AXES_LOCKOUT_URL = '/account_locked/'
AXES_RESET_ON_SUCCESS = True # RESETEA EL CONTADOR DE LOS FALLOS CUANDO HAY LOGIN EXITOSO

# CONFIGURACIÓN DEL LOGIN Y LOGOUT

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# CONFIGURACIÓN DE MENSAJES
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # AXES
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'TallerRayoMakween.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.user_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'TallerRayoMakween.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
	'default': {
        'ENGINE' : 'django.db.backends.postgresql_psycopg2',
        'HOST' : 'aws-0-sa-east-1.pooler.supabase.com',
        'NAME' : 'postgres',
        'USER' : 'postgres.yzfmhvawgcsetsotiuid',
        'PASSWORD' : 'Juan1473!"#$%&/()',
        'PORT' : '5432'
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

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
