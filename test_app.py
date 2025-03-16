import pytest
from flask import json
from app import product_service  # depuis app.py

@pytest.fixture
def client():
    #Créer un client de test Flask
    return product_service.test_client()

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Bienvenue sur le service des produits" in response.data

def test_get_products(client):
    response = client.get("/product")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert len(data) >= 1  # si il y a au moins 1 produit

# teste POST
def test_post_product(client):
    new_product = {"id": 3, "name": "MacBook Pro", "price": 2500}
    response = client.post("/product", data=json.dumps(new_product), content_type="application/json")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["message"] == "Product added"
    assert data["product"] == new_product

if __name__ == "__main__":
    pytest.main()