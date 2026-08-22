from unittest.mock import patch


@patch("app.routes.project.service.list_projects")
def test_unexpected_error_returns_safe_500(mock_list_projects, client):
    mock_list_projects.side_effect = Exception("Sensitive internal detail")
    
    response = client.get("/projects")
    
    data = response.get_json()
    
    assert response.status_code == 500
    
    assert data['error']['message'] == "An unexpected error occured"
    
    assert data['error']['code'] == "internal_server_error"
    
    assert "Sensitive internal detail" not in str(data)