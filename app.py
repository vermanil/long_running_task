from flask import Flask, render_template
from os import environ
from celery import Celery, shared_task
# from tasks import dine
import request

def make_celery(app):
    # set redis url vars
    app.config['CELERY_BROKER_URL'] = environ.get('REDIS_URL', 'redis://localhost:6379/0')
    app.config['CELERY_RESULT_BACKEND'] = app.config['CELERY_BROKER_URL']
    app.config['CELERY_IMPORTS'] = ("tasks",)
    # create context tasks in celery
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask

    return celery

app = Flask(__name__)
celery = make_celery(app)

@app.route('/')
def landing_page():
    return render_template('fileUpload.html')

@app.route('/upload-file')
def upload_file(*args, **kwargs):
    # dine.apply_async(*args, **kwargs)
    hello_task.apply_async(*args, **kwargs)
    return render_template('fileUpload.html')

@celery.task
def hello_task(*args, **kwargs):
	print "dhbhfdbfhgbfhdj"

if __name__ == "__main__":
    app.run(debug = True)