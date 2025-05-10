from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# M-Pesa API Config from .env
MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')
MPESA_ENV = os.getenv('MPESA_ENV', 'sandbox')  # default to sandbox
MPESA_CALLBACK_URL = os.getenv('MPESA_CALLBACK_URL')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qx89307sqa-h1jo0$45vt*zvwnf5w$nw_cc9sng)tmz4-xg9k2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_bootstrap5",
    'myapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/



TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/


LANGUAGE_CODE = 'en-us'



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Make sure BASE_DIR is defined
] if os.path.exists(os.path.join(BASE_DIR, "static")) else []



# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'myapp.CustomUser'


AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'publicpages.authentication.EmailBackend',  # Custom email authentication
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication
]

SESSION_ENGINE = "django.contrib.sessions.backends.db"  # Uses the database
SESSION_COOKIE_AGE = 1209600  # 2 weeks (matches your logic)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep session alive even after closing the browser

# Redirect users to the homepage or dashboard after login
LOGIN_URL = '/login/' 
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "ramspheldonyango@gmail.com"
EMAIL_HOST_PASSWORD = "qakp qgtr inpn sapv"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


PAYPAL_CLIENT_ID = "ATkLED_rdrWQKqEWQteX4mV1CDpTgeJpKOHcFTsDO0D5sVOHEE5I8NvQP3CEBGoX-xYe-gXoAzjatjn3"
PAYPAL_CLIENT_SECRET = "ENNnPpE3bP_dyt9QzAqvM6cAttMsLTB7uJS01-OcBJhFqOtceVRIxp1DI2SlzL0-WYSjqN16QKgZv8_k"
PAYPAL_MODE = "sandbox"  # Change to "live" for real payments