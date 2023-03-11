from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from product import Product

db = dbase.dbConnection()

app = Flask(__name__)

# rutas de la app
@app.route("/")
def home ():
    return render_template("index.html")

#method post
@app.route("/products", methods=["POST"])
def addProduct():
    products = db["products"]
    name = request.form["name"]
    price = request.form["price"]
    quantity = request.form["quantity"]
    
    if name and price and quantity:
        product = Product(name,price,quantity)
        products.insert_one(product.toDBCollection())
        response = jsonify ({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        return redirect(url_for("home"))
    else:
        return notFound()

#method delete
@app.route("/delete/<string:product_name>")
def delete(product_name):
    products = db["products"]
    products.delete_one({"name": product_name})
    return redirect(url_for("home"))

#method put
@app.route("/edit/<string:product_name>", methods=["POST"])
def edit(product_name):
    products = db["products"]
    name = request.form["name"]
    price = request.form["price"]
    quantity = request.form["quantity"]
    
    if name and price and quantity:
        products.update_one({"name" : product_name}, {"$set" : {"name" : name, "price" : price, "quantity" : quantity}})
        response = jsonify({"message" : "Producto" + product_name + "actualizado correctamente"})
        return
    
@app.errorhandler(404)
def notFound(error=None):
    message = {
        "message": "no encontrado" + request.url,
        "status": "404 not found"
    }
    response = jsonify(message)
    response.status_code = 404
    return response
        
        
        
        
if __name__ == "__main__":
    app.run (debug=True, port=5000)

#https://www.youtube.com/watch?v=A05cBJ_P7Q8 minuto 30
