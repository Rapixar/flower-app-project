DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'floweapp',
        'USER': 'floweapp',
        'PASSWORD': 'floweapp',
        'HOST': 'localhost',
        'PORT': ''
    }
}
#################################################################
##  (CORS) Cross-Origin Resource Sharing Settings ##
#################################################################
CORS_ORIGIN_ALLOW_ALL = True
