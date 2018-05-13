from celery import Celery
from os import environ

def configure_celery(app):
    # set redis url vars
    app.config['CELERY_BROKER_URL'] = environ.get('REDIS_URL', 'redis://localhost:6379/0')
    app.config['CELERY_RESULT_BACKEND'] = app.config['CELERY_BROKER_URL']

    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    
    return celery