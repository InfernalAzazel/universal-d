"""
后台项目的 Django 设置.

由 'django-admin startproject' 使用 Django 5.0.3 生成.

有关此文件的详细信息，请参阅
https://docs.djangoproject.com/en/5.0/topics/settings/

有关设置及其值的完整列表，请参阅
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
import environ
from pathlib import Path

# 像这样在项目内部构建路径：BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 环境变量
env = environ.Env()
# 从 .env 文件中获取环境变量
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# 快速启动开发设置 - 不适合生产环境
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# 安全警告：对生产中使用的密钥保密!
SECRET_KEY = env.str("SECRET_KEY", 'django-insecure-3)ksab@cp(ht-biejct$1hk4@+@+k@se-e7uc7r*+m5facw3vl')

# 安全警告：不要在生产环境中打开调试的情况下运行！
DEBUG = env.bool('DEBUG', True)

ALLOWED_HOSTS = []

# 应用程序定义
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "apps.apps.AppsConfig"
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

ROOT_URLCONF = 'backend.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'

# 数据库
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': env.str('DATABASE_ENGINE', 'django.db.backends.postgresql'),
        'NAME': env.str('DATABASE_NAME', 'universal'),
        'USER': env.str('DATABASE_USER', 'spb0122003'),
        'PASSWORD': env.str('DATABASE_PASSWORD', 'dcaGRzkJpuKsHgMs8hoS'),
        'HOST': env.str('DATABASE_HOST', 'localhost'),
        'PORT': env.str('DATABASE_HOST', '5432'),
    }
}

# 密码验证
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

# 国际化
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# 静态文件 (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# 默认主键字段类型
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
