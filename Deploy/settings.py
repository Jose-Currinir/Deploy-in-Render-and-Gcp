import json
import os
from pathlib import Path
import environ
from dotenv import load_dotenv
import dj_database_url
from google.oauth2 import service_account
"""
1.  Comenzamos con los imports que se encuentran aquí arriba
2.  Comenzamos con implementar el código que posee al lado derecho el comentario #Código deploy
3.  En general el código marcado como deploy, será explicado a continuación
3.1.    En la sección de load_dotenv.Env() es donde inicializamos las variables de entorno que utilizaremos dentro de render.com
3.2.    Las variables de entorno que posee el proyecto, son las siguientes.
        DATABASE_URL
        DEBUG
        GOOGLE_APPLICATION_CREDENTIALS
        PYTHON_VERSION
        SECRET_KEY
3.3.    

"""
load_dotenv()           #Código deploy
env = environ.Env()     #Código deploy
environ.Env.read_env()  #Código deploy
ENVIRONMENT = env       #Código deploy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')   #Código deploy
SITE_NAME = 'Primera CBPA'                  #Código deploy
DEBUG = 'RENDER' not in os.environ          #Código deploy

ALLOWED_HOSTS = [
    "localhost",                #Código deploy
    "127.0.0.1"                 #Código deploy
]
if not DEBUG:                   #Código deploy
    ALLOWED_HOSTS = [           #Código deploy
        "curri.cl",             #Código deploy
        ".curri.cl",            #Código deploy
        "www.curri.cl"          #Código deploy
    ]
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')   #Código deploy
if RENDER_EXTERNAL_HOSTNAME:                                            #Código deploy
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)                      #Código deploy

DJANGO_APPS = [                     #Código deploy
    'django_dump_load_utf8',        #Código deploy
    'jazzmin',                      #Código deploy
    'django.contrib.sitemaps'       #Código deploy
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
PROJECT_APPS = [                    #Código deploy
    'apps.webpage',                 #Código deploy
    #'apps.inventory'               #Código deploy
]
THIRD_PARTY_APPS = [                #Código deploy
    'bootstrap5',                   #Código deploy
    'storages',                     #Código deploy
]
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS      #Código deploy


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',                   #Código deploy
]

ROOT_URLCONF = 'Deploy.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],              #Código deploy
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

WSGI_APPLICATION = 'Deploy.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {                                           #Código deploy
    'default': dj_database_url.config(                  #Código deploy
        default= os.environ.get('DATABASE_URL'),        #Código deploy  //  
        conn_max_age=600                                #Código deploy
    )
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'es-CL'         #Código deploy
TIME_ZONE = 'America/Santiago'  #Código deploy
USE_I18N = True                 #Código deploy
USE_TZ = True                   #Código deploy

# Archivos estaticos                                                                        #Código deploy
STATIC_URL = '/static/'                                                                     #Código deploy
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]                                       #Código deploy
if not DEBUG:                                                                               #Código deploy
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')                                     #Código deploy
    #STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'        #Código deploy
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'           #Código deploy

# Archivos media                                                #Código deploy
MEDIA_URL = '/media/'                                           #Código deploy 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')                    #Código deploy

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'            #Código deploy
AUTHENTICATION_BACKENDS = (                                     #Código deploy
    'django.contrib.auth.backends.ModelBackend',                #Código deploy
)                                                               #Código deploy
FILE_UPLOAD_PERMISSIONS = 0o640                                 #Código deploy
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'  #Código deploy

#   Conexión con el bucket de google
if not DEBUG:
    GS_BUCKET_NAME = 'cv-jose'
    STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
    credenciales_json = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if credenciales_json:
        credenciales_dict = json.loads(credenciales_json)
        GS_CREDENTIALS = service_account.Credentials.from_service_account_info(credenciales_dict)
    else:
        GS_CREDENTIALS = None
        GS_CREDENTIALS = service_account.Credentials.from_service_account_info(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'))