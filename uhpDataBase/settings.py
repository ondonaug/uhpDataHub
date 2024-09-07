"""
Django settings for uhpDataBase project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yp@yq=yq8^s3uu^nrgq47_jgtckb4i4^rps66)8bi0%_3&#5yc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*'] # For local 
#ALLOWED_HOSTS = ['https://uhpcdb-d5exeph6b4hhfge7.westeurope-01.azurewebsites.net'] # For deployement
CSRF_TRUSTED_ORIGINS = ['https://uhpcdb-d5exeph6b4hhfge7.westeurope-01.azurewebsites.net']
# security.W016
CSRF_COOKIE_SECURE = False

# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_static_jquery',
    'myUHP.apps.MyuhpConfig',
    'crispy_bootstrap4',
    'crispy_forms',
    'widget_tweaks',
    'import_export',
    'lockdown',
]

LOCKDOWN_PASSWORDS = ('david', '1234')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_auto_logout.middleware.auto_logout', # Django auto logout (1)
]

ROOT_URLCONF = 'uhpDataBase.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_auto_logout.context_processors.auto_logout_client', # Django auto logout (2)
            ],
        },
    },
]

WSGI_APPLICATION = 'uhpDataBase.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
     #   'NAME': BASE_DIR / 'db.sqlite3',
         'ENGINE': 'django.db.backends.mysql',
       # 'NAME': 'ylpmjzzgdo$uhpcdb-database',
         'NAME': 'uhpdatabase',
         'USER':'ylpmjzzgdo',
         'PASSWORD':'$cGy4BjroDQMMmPn',
         'HOST':'uhpcdb-server.mysql.database.azure.com',
         'PORT':3306,
         'OPTION':{
                'init_command':"SET sql_mode=STICT_TRANS_TABLES"
           }
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


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')] # for deploy use staticfiles
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # for deploy use static


AUTO_LOGOUT = {'IDLE_TIME': 1200, 'REDIRECT_TO_LOGIN_IMMEDIATELY': True,
               'MESSAGE': 'The session has expired. Please login again to continue.',}  # logout after 10 minutes of downtime (4)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DYNAMIC_DATATB={
    'workplans':"app.models.Operworkplan",
}
