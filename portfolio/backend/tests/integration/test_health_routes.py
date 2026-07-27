def test_health_endpoint_returns_success(client):
    response = client.get("/health")
    
    assert response.status_code == 200
    
    
def test_health_endpoint_returns_json(client):
    response = client.get("/health")
    
    assert response.is_json
    

def test_health_endpoint_response_body(client):
    response = client.get("/health")
    
    data = response.get_json()
    
    assert data["status"] == "ok"
    assert data["service"] == "backend"
    
    
