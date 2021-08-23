from .settings import *

DEBUG = True

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'HOST': env('DB_HOST'),
		'DATABASE_PORT': env('DB_PORT'),
		'NAME': env('DB_NAME'),
		'USER': env('DB_USER'),
		'PASSWORD': env('DB_PASSWORD')
	}
}

ALLOWED_HOSTS += ["127.0.0.1", 'localhost']
