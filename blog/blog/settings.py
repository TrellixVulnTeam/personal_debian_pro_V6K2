"""
项目配置文件；
项目名称：myblog

Django settings for myblog project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import pymysql  #使用mysql数据库

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%oyd37a)%mh0@zts7b)ki5f1u(ibiw9z%6w9-khmz^gvrd+3&2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jet', #django-jet settings,before the django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myblog',
    'corsheaders',
    # 'wtoken',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', #jet settings
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

PASSWORD_HASHERS = (
     'django.contrib.auth.hashers.PBKDF2PasswordHasher',
     'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
     'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
     'django.contrib.auth.hashers.BCryptPasswordHasher',
     'django.contrib.auth.hashers.SHA1PasswordHasher',
     'django.contrib.auth.hashers.MD5PasswordHasher',
     'django.contrib.auth.hashers.CryptPasswordHasher',
)


WSGI_APPLICATION = 'blog.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog_db',     # 数据库名称
        'USER': 'root',        # mysql 账号
        'PASSWORD': '166891',  # mysql 密码
        'HOST': 'localhost',   # 如果不能连接，改成localhost
        'POST': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# 配置用户上传的文件
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 需要配置TEMPLATES

# UserProfile 覆盖了 django 内置的 users 表
AUTH_USER_MODEL = 'myblog.user'

APPEND_SLASH=False  #可以在应用urls加斜杠

CORS_ORIGIN_ALLOW_ALL = True #允许所有域名跨域
#或者配置跨域白名单
#CORS_ORIGIN_WHITELIST = {
    #106.12.124.116:8000
#    '*'
#}

#允许携带cookies
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = {
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
}

CORS_ALLOW_HEADERS = {
    'XMLHttpRequest',
    'X_FILENAME',
    'accept',
    'accept-encode',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
}

if __name__ == "__main__":
    import os,django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")# project_name 项目名称
    django.setup()

    from django.contrib.auth.hashers import make_password, check_password
    pwd=''
    mpwd=make_password(pwd,'pbkdf2_sha256')  # 创建django密码，第三个参数为加密算法
    print(mpwd)
    pwd_bool=check_password(pwd,'pbkdf2_sha256$100000$JteXYgDMOsbz$zVzsA7mDW0UAb5k6SM0e9x5Sdlh/PKKwSekyDnDmQYg=')# 返回的是一个bool类型的值，验证密码正确与否
    print("我曹无情：",pwd_bool)
