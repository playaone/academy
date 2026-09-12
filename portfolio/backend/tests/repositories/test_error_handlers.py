from unittest.mock import patch


@patch("app.routes.project.service.list_projects")
def test_unexpected_error_returns_safe_500(mock_list_projects, client):
    mock_list_projects.side_effect = Exception("Sensitive internal detail")

    response = client.get("/projects")

    data = response.get_json()

    assert response.status_code == 500

    assert data["error"]["message"] == "An unexpected error occured"

    assert data["error"]["code"] == "internal_server_error"

    assert "Sensitive internal detail" not in str(data)


def test_unknown_route_returns_json_404(client):
    response = client.get("/non-existent-route")

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"]["code"] == "not_found"


def test_unsupported_http_method_returns_405(client):
    response = client.put("/projects")

    data = response.get_json()

    assert response.status_code == 405

    assert data["error"]["code"] == "method_not_allowed"


def test_application_error_uses_error_contract(client):
    response = client.get("/projects/9999")

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"]["code"] == "resource_not_found"
    assert data["error"]["message"] == "Project not found"


@patch("app.error_handlers.db.session.rollback")
@patch("app.routes.project.service.list_projects")
def test_unexpected_error_rolls_back_session(mock_list_projects, mock_rollback, client):
    mock_list_projects.side_effect = RuntimeError("boom")

    response = client.get("/projects")

    assert response.status_code == 500
    mock_rollback.assert_called_once()
