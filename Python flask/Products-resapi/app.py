from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

#ruta prueba#

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "moisesgai!"})

# Home #
@app.route("/", methods=["GET"])
def getUrl():
    return "Home"

#Ruta products#

@app.route("/products", methods=["GET"])
def getProducts():
    return jsonify({"products": products, "message": "Products list"}) # retorna un objeto

# imprimir una lista y recorrerla #

@app.route("/products/<string:product_name>", methods=["GET"]) # :product_name
def getProduct(product_name):
    productsFound = [product for product in products if product["name"] == product_name]    #recorre la lista de productos y la compara para retornar
    if (len(productsFound)>0):
        return jsonify ({"product": productsFound[0]})
    return jsonify ({"message": "Product not found"})

# Agregar un dato #

@app.route("/products", methods=["POST"])
def addProduct():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "Product add Succesfully", "products": products})

# Actualizar #
@app.route("/products/<string:product_name>", methods=["PUT"])
def editProduct(product_name):
    productFound = [product for product in products if product["name"] == product_name]
    if(len(productFound)> 0):
        productFound[0]["name"] = request.json["name"]
        productFound[0]["price"] = request.json["price"]
        productFound[0]["quantity"] = request.json["quantity"]
        return jsonify({
            "message": "product updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product Not Found"})    
# Eliminar #
@app.route("/products/<string:product_name>", methods=["DELETE"])
def deleteProduct(product_name):
    productFound = [product for product in products if product["name"] == product_name]
    if (len(productFound)>0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Product deleted",
            "products": products
        })
    return jsonify({"message": "Product Not Found"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    
#20:30

