"""
Django settings for eshop_project project.
"""

from pathlib import Path

# ───────────────────────────────────────────
# BASE DIR
# ───────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

# ───────────────────────────────────────────
# CORE SETTINGS
# ───────────────────────────────────────────
SECRET_KEY = 'django-insecure-*lj^j+jtg%l(2o_4x+6&4=h%zp%5*s5w626(2l*^mt8v&$7kjm'
DEBUG = True
ALLOWED_HOSTS = [
    '45.13.132.172',
    'localhost',
    '127.0.0.1',
    'mitsubishifabd.com',
]

# ───────────────────────────────────────────
# INSTALLED APPS
# ───────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party / project apps
    'rest_framework',
    'widget_tweaks',
    'mptt',

    # local app
    'eshop',
]

# ───────────────────────────────────────────
# JAZZMIN SETTINGS (sample)
# ───────────────────────────────────────────
JAZZMIN_SETTINGS = {
    "site_title": "My eShop Admin",
    "site_header": "My eShop Admin",
    "site_brand": "My eShop",
    "login_logo": None,           # e.g. "images/logo.png"
    "show_sidebar": True,
    "navigation_expanded": True,
}

# ───────────────────────────────────────────
# MIDDLEWARE
# ───────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eshop_project.urls'

# ───────────────────────────────────────────
# TEMPLATES
# ───────────────────────────────────────────
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'eshop' / 'templates',
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'eshop_project.wsgi.application'

# ───────────────────────────────────────────
# DATABASE
# ───────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ───────────────────────────────────────────
# PASSWORD VALIDATORS
# ───────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ───────────────────────────────────────────
# INTERNATIONALIZATION
# ───────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ───────────────────────────────────────────
# STATIC & MEDIA
# ───────────────────────────────────────────
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'eshop' / 'static']
STATIC_ROOT    = BASE_DIR / 'staticfiles'       # ←★ This line MUST be present

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ───────────────────────────────────────────
# EMAIL (console backend for dev)
# ───────────────────────────────────────────
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
