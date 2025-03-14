from flask import Flask, request, jsonify


# ________________________________MICROSERVICE 1_________________________


product_service = Flask("product_service")
@product_service.route("/", methods=["GET"])
def home():
    return """
        <h1>Bienvenue sur le service des produits</h1>
        <p>Consultez la liste des produits ici : <a href="http://127.0.0.1:4000/product">Liste des produits</a></p>
    """

# ma liste de produit
product = [
    {"id": 1, "name": "PC", "price": 1200},
    {"id": 2, "name": "SAMSUNG", "price": 800}
]

@product_service.route("/product" , methods = ["GET" , "POST"])
def product_manager() :
    if request.method == "GET" :
        return jsonify(product)
    elif request.method == "POST" :
        data = request.get_json()
        product.append(data)
        return jsonify({"message": "User added", "user": data})


if __name__ == "__main__" :

    product_service.run(debug = True , host='0.0.0.0',port=5000)