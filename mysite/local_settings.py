import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mydb3',
        'USER': 'postgres',
        'PASSWORD': 'evyfz553157',
        'HOST': '127.0.0.1',
        'PORT': '5432',
       # 'OPTIONS': {
        #            'options': '-c search_path=dictionaries,clinical_trial,disease,drug,patient_group,article_research,article,clinical_trial'
        #        }
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR, ]
STATIC_URL = '/static/'
