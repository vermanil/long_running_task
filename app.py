from flask import Flask, render_template
from os import environ
from celery import Celery, shared_task

app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('fileUpload.html')

@app.route('/upload-file')
def upload_file(*args, **kwargs):
    background_task.delay(*args, **kwargs)
    return render_template('fileUpload.html')

def make_celery(app):
    # set redis url vars
    app.config['CELERY_BROKER_URL'] = environ.get('REDIS_URL', 'redis://localhost:6379/0')
    app.config['CELERY_RESULT_BACKEND'] = app.config['CELERY_BROKER_URL']
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

celery = make_celery(app)

@celery.task
def background_task(*args, **kwargs):
	print "dhbhfdbfhgbfhdj"

if __name__ == "__main__":
    app.debug = True
    app.run()