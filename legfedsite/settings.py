import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for legfedsite project.

Generated by 'django-admin startproject' using Django 1.11.13.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oq=$uz2u_xzlsi%o5-*f4#h2q=$2zkb8-m^w6aqm0g214tys!2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','legfeddev','fisher','fisher.ncgr.org']


# Application definition

ROOT_URLCONF = 'legfedsite.urls'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Denver'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'legfedsite', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'legfedsite', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE = (
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'filer',
    'easy_thumbnails',
    'aldryn_apphooks_config',
    'cmsplugin_filer_image',
    'cmsplugin_form_handler',
    'parler',
    'taggit',
    'taggit_autosuggest',
    'meta',
    'sortedm2m',
    'adminsortable2',
    'aldryn_boilerplates',
    'aldryn_faq',
    'aldryn_disqus',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'djangocms_blog',
    'djangocms_column',
    'djangocms_file',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',
    'djangocms_forms',
    'legfedsite',
    'polls',
    'polls_cms_integration',
    'species_mgr.apps.SpeciesMgrConfig',
    'resource_mgr.apps.ResourceMgrConfig',
    'announcements.apps.AnnouncementsConfig',
    'announcements_cms_integration',
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('English')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('English'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature'),
    ('home.html', 'Home Page'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}


DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': '/home/svengato/legfed-django-site/project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

META_SITE_PROTOCOL = 'http'
META_USE_SITES = True

ALDRYN_BOILERPLATE_NAME='legacy'

DISQUS_SHORTNAME = 'legfed'

DJANGOCMS_FORMS_PLUGIN_MODULE = ('Generic')
DJANGOCMS_FORMS_PLUGIN_NAME = ('Form')
DJANGOCMS_FORMS_DEFAULT_TEMPLATE = 'djangocms_forms/form_template/default.html'
DJANGOCMS_FORMS_USE_HTML5_REQUIRED = False
DJANGOCMS_FORMS_REDIRECT_DELAY = 1000  # 1 second

TWITTER_FEED_CONSUMER_PUBLIC_KEY = 'iuF1VSu4dawtFt3Bfq3ZgLcOC'
TWITTER_FEED_CONSUMER_SECRET = 'uw0vO4hjulUXuPXZtO2WNJcDmBjtQCejxPJ3ngcZW6lXDZhX9s'
TWITTER_FEED_OPEN_AUTH_TOKEN = '3142058411-rWQb0louKgHtaV8MVrmMDu2HktbX0smTRubxJMr'
TWITTER_FEED_OPEN_AUTH_SECRET = 'DRHubi2sY7X7X43SmZg2IjnKkZ9iP6LLkdK3zlfbeGL45'

# Your access token: Access token
TWITTER_OAUTH_TOKEN = '3142058411-rWQb0louKgHtaV8MVrmMDu2HktbX0smTRubxJMr'
# Your access token: Access token secret
TWITTER_OAUTH_SECRET = 'DRHubi2sY7X7X43SmZg2IjnKkZ9iP6LLkdK3zlfbeGL45'
# OAuth settings: Consumer key
TWITTER_CONSUMER_KEY = 'iuF1VSu4dawtFt3Bfq3ZgLcOC'
# OAuth settings: Consumer secret
TWITTER_CONSUMER_SECRET = 'uw0vO4hjulUXuPXZtO2WNJcDmBjtQCejxPJ3ngcZW6lXDZhX9s'
