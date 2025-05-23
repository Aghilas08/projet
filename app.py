from flask import Flask, request, jsonify

# Acceil

product_service = Flask("product_service")
@product_service.route("/", methods=["GET"])
def home():
    return """
        <html>
            <head><title>Service Produits</title></head>
            <body style="font-family: Arial; padding: 20px;">
                <h1>Bienvenue sur le service des produits</h1>
                <p>Consultez la liste des produits ici :
                <a href="/product">Liste des produits</a>
                </p>
            </body>
        </html>
    """


# product_service

# data == ma liste de produit
product = [    
    {"id": 1, "name": "PC", "price": 1200},
    {"id": 2, "name": "SAMSUNG S24", "price": 1300}
]

@product_service.route("/product" , methods = ["GET" , "POST"])
def product_manager() :
    if request.method == "GET" :
        return jsonify(product)
    elif request.method == "POST" :
        data = request.get_json()
        product.append(data)
        return jsonify({"message": "Product added", "product": data})


if __name__ == "__main__" :

    product_service.run(debug = True , host='0.0.0.0',port=5000)