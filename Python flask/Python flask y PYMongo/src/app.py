from flask import Flask, request, jsonify, Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash,check_password_hash
from bson import json_util
from bson.objectid import ObjectId


app = Flask(__name__)   
app.config["MONGO_URI"]="mongodb://localhost:27017/local.users"
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
    # Se valida si existe el correo electronico
    
    #if mongo.db.users.find({"email" : email}) : 
        #return {"message": "user alredy exists"}
    # Se valida si exisre el id
    #if mongo.db.users.find({"_id" : _id}):
        #return {"message": "id alredy exists"}
    
    # se incripta el la clave
    if username and email and password:
        hashed_password = generate_password_hash(password)
    #se mandan los datos
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
        return not_found()
    
    return {"message" : "received"}
# Consulta *
@app.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")

# Consulta especifica
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(user)
    return Response (response, mimetype="application/json")

# Borrar
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    mongo.db.users.delete_one({"_id": ObjectId(id)})
    response = jsonify({"message": "user" + id + "was deleted successfully"})
    return response
# actualizar
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    username = request.json["username"]
    password = request.json["password"]
    email = request.json["email"]
    if username and email and password:
        hashed_password = generate_password_hash(password)
        mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": {
            "username" : username,
            "password" : hashed_password,
            "email" : email    
        }})
        responde = jsonify({"message": "user" + id + "was updated successsfully"})
        return responde
        

# ERRORES
@app.errorhandler(404)
def not_found(error=None):
    message = jsonify({
        "message" : "resource not found: " + request.url,
        "status": 404
    })
    message.status_code = 404
    return message
        



if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
