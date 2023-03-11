from pymongo import MongoClient
import certifi

MONGO_URI = "mongodb+srv://Akari:<ConquerorEnJoyer>@xd.kvv8olg.mongodb.net/?retryWrites=true&w=majority"
ca = certifi.where()

def dbConnection():
    try:
        cliente = MongoClient.connect(MONGO_URI, tlsCAFile=ca)
        db = cliente["XD"]
    except ConnectionError:
        print("error de conexion con la bdd")
    return db       
