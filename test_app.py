from app import product_service

def test_home() :
    reponse = product_service.test_home().get("/")

    assert reponse.status_code == 200