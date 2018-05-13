from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Task, FileInfo
from celery_config import configure_celery

app = Flask(__name__)
celery = configure_celery(app)

# Databse connection
engine = create_engine('sqlite:///long_running_task.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
dbsession = DBSession()

@app.route('/')
def landing_page():
    # print dbsession.query(Task).all()
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