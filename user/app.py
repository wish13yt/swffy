from flask import Flask, request, send_from_directory, abort
from werkzeug.utils import secure_filename
import scrypt
import flask_cors as flco

app = Flask(__name__)
flco.CORS(app)
@app.route('/api/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['flash']
        if not secure_filename(f.filename).endswith(".swf"):
            return "rejected: file type incorrect"
        with open("db/swf/largestid.txt", "r") as grf:
            num = int(grf.read())
        thenumber = num + 1
        if num == "0":
            thenumber = 1
        f.save(f"db/swf/{thenumber}")
        with open("db/swf/largestid.txt", "w") as grfw:
            grfw.write(thenumber)
        return "Submitted! An admin will review your file and approve or reject it. You won't be notified if it is accepted or rejected."

@app.route('/api/getswf', methods=['GET', 'POST'])
def getswf():
    swfname = request.form['swfname']
    return send_from_directory('../db/swf/', swfname + ".swf", as_attachment=True)

@app.route('/api/approve')
def approve():
    password = request.form['passw']
@app.route('/api/signin', methods=["POST"])
def signin():
    pw = request.form['passw']
    try:
        with open("adminpw.bin", "rb") as f:
            realpw = f.read()
            f.close()
        g = scrypt.decrypt(realpw, pw)
        print("DECRYPTED:" + str(g))
        executed = True
        realpw = "abcdefgh"
    except Exception as e:
        realpw = "abcdefgh"
        print(str(e))
        abort(401, "Password incorrect")
    if executed == True:
        realpw = "abcdefgh" #what
        #to get rid of the variable
        #o
        return "success", 200