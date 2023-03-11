from pymongo import MongoClient

#MONGO_URI = "pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.kzfpgmi.mongodb.net/?retryWrites=true&w=majority")"
MONGO_URI = "mongodb://localhost:27017"

def dbConnection():
    try:
        cliente = MongoClient(MONGO_URI)
        db = cliente.XD
    except ConnectionError:
        print("error de conexion con la bdd")
    return db       
