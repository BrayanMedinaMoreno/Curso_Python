from flask import Flask,jsonify,render_template,request
from werkzeug.utils import secure_filename
import os 

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/uploads"

ALLOMED_EXTENSIONS = set(["jpg","png","gif","mp4"])

def allowed_file (file):
    file = file.split(".")
    print(file)
    if file[1] in ALLOMED_EXTENSIONS:
        return True
    return False
    

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload" ,methods=["POST"])
def upload():
    file = request.files["uploadFile"]
    print(file,file.filename)
    filename = secure_filename(file.filename)
    print(filename)
    #allowed_file()
    #print(allowed_file)
    if file and allowed_file(filename):
        print("permitido")
        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        return render_template("index.html",mesaje="Archivo subido con exito" )
    return render_template("index.html",mesaje="Archivo Fracaso son exito sapo hpt" )
 

if __name__ == "__main__":
    app.run(debug=True,port="5000")
