from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('fileUpload.html')

@app.route('/upload-file')
def upload_file():
    return render_template('fileUpload.html')

if __name__ == "__main__":
    app.debug = True
    app.run()