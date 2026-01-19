from flask import Flask, request, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['flash']
        f.save(f'../db/swf/{secure_filename(f.filename)}.swf')
        return "Submitted! An admin will review your file and approve or reject it. You won't be notified if it is accepted or rejected."

@app.route('/api/getswf', methods=['GET', 'POST'])
def getswf():
    swfname = request.form['swfname']
    return send_from_directory('../db/swf/', swfname + ".swf", as_attachment=True)

@app.route('/api/approve')
def approve():
    password = request.form['passw']