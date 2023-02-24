from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)   
app.config["MONGO_URI"]="mongodb://localhost:27017/local"
mongo = PyMongo(app)

#Home#

@app.route("/", methods=["GET"])
def create_Home(): 
    return "received" 


#post#
@app.route("/users", methods=["POST"])
def create_User():
    # recive datos
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]
    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one(
            {"username": username,"email": email,"password": hashed_password}
        )
        response = {
            "id": str(id),
            "username": username,
            "password": hashed_password,
            "email": email
        }
        return response
    else:
        {"message":"received"}
        



if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
