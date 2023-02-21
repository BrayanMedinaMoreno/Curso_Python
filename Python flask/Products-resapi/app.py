from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

#ruta prueba#

@app.route("/ping")
def ping():
    return jsonify({"message": "moisesgai!"})

#Ruta products#

@app.route("/products")
def getProducts():
    return jsonify({"products": products, "message": "Products list"}) # retorna un objeto

# imprimir una lista y recorrerla #

@app.route("/products/<string:product_name>") # :product_name
def getProduct(product_name):
    productsFound = [product for product in products if product["name"] == product_name]    #recorre la lista de productos y la compara para retornar
    if (len(productsFound)>0):
        return jsonify ({"product": productsFound[0]})
    return jsonify ({"message": "Product not found"})

# hacer un post #

@app.route("/products", methods=["POST"])
def addProduct():
    print(request.json)
    return "received"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
#20:30

