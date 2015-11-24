# coding=utf-8
import os.path
import sys


PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__),".."))
PROJECT_SRC_ROOT = os.path.normpath(os.path.join(PROJECT_ROOT, 'src'))
if PROJECT_SRC_ROOT not in sys.path:
    sys.path.insert(0,PROJECT_SRC_ROOT )
    
INTERNAL_IPS = ( )

ADMINS = ( )

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'ru-ru'
USE_I18N = True

DATE_FORMAT = "j E Y г."
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = 'j E Y г. – H:i'


MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')
# fastcgi fix
FORCE_SCRIPT_NAME = ''

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'src', 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
if not hasattr(globals(), 'SECRET_KEY'):
    SECRET_FILE = os.path.join(PROJECT_ROOT, 'secret.txt')
    try:
        SECRET_KEY = open(SECRET_FILE).read().strip()
    except IOError:
        try:
            from random import choice
            SECRET_KEY = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
            secret = file(SECRET_FILE, 'w')
            secret.write(SECRET_KEY)
            secret.close()
        except IOError:
            raise Exception('Please create a %s file with random characters to generate your secret key!' % SECRET_FILE)

ROOT_URLCONF = "urls"

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
)


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.admin",
    "django.contrib.sessions",
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    "south",
]

# LOGIN_URL = '/smartlogin/'
# LOGOUT_URL = '/ke/passport/logout/'




DEBUG = True
TEMPLATE_DEBUG = False
