from flask import Flask, render_template
from os import environ
from celery import Celery

def configure_celery(app):
    # set redis url vars
    app.config['CELERY_BROKER_URL'] = environ.get('REDIS_URL', 'redis://localhost:6379/0')
    app.config['CELERY_RESULT_BACKEND'] = app.config['CELERY_BROKER_URL']

    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    
    return celery

app = Flask(__name__)
celery = configure_celery(app)

@app.route('/')
def landing_page():
    return render_template('fileUpload.html')

@app.route('/upload-file')
def upload_file(*args, **kwargs):
    hello_task.delay(*args, **kwargs)
    return render_template('fileUpload.html')

@celery.task
def hello_task(*args, **kwargs):
	print "dhbhfdbfhgbfhdj"

if __name__ == "__main__":
    app.run(debug = True)