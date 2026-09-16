from unittest.mock import patch

import pytest

from tests.factories.project_factory import build_project_data, create_project_via_api

# payload = {
#     "title": "Engineering Journey Platform",
#     "description": "A full-stack portfolio platform",
#     "github_url": "https://github.com/example/project",
#     "website_url": "https://example.com"
# }
# payload2 = {
#     "title": "Engineering Journey Platform 2",
#     "description": "A full-stack portfolio platform 2",
#     "github_url": "https://github.com/example/project/2",
#     "website_url": "https://example.com/2"
# }

payload = build_project_data(
    github_url="https://github.com/example/project", website_url="https://example.com"
)
payload2 = build_project_data(
    sequence=2,
    github_url="https://github.com/example/project/2",
    website_url="https://example.com/2",
)


def test_create_project_returns_201(client):

    response = create_project_via_api(client)

    assert response.status_code == 201


def test_create_project_returns_created_project(client):
    response = create_project_via_api(
        client, github_url=payload["github_url"], website_url=payload["website_url"]
    )

    data = response.get_json()

    assert data["id"] is not None
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["github_url"] == payload["github_url"]
    assert data["website_url"] == payload["website_url"]


def test_create_project_without_title_returns_400(client):
    test_payload = {"description": "A project without a title"}

    response = client.post("/projects", json=test_payload)

    data = response.get_json()

    assert response.status_code == 400

    assert data["error"]["code"] == "validation_error"
    assert data["error"]["message"] == ("Request validation failed")


def test_create_project_with_invalid_json_returns_400(client):
    response = client.post(
        "/projects", data="{'title':", content_type="application/json"
    )

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"]["code"] == "validation_error"
    assert data["error"]["message"] == ("Request body must contain valid JSON")


def test_create_duplicate_project_returns_409(client):
    first_response = create_project_via_api(client)

    second_response = create_project_via_api(client)

    data = second_response.get_json()

    assert first_response.status_code == 201
    assert second_response.status_code == 409

    assert data["error"]["code"] == "conflict"


def test_list_projects_returns_created_projects(client):
    create_project_via_api(client)

    client.post("/projects", json=payload2)

    response = client.get("/projects")

    data = response.get_json()

    titles = {project["title"] for project in data["items"]}

    assert response.status_code == 200
    assert len(data["items"]) == 2

    assert titles == {payload["title"], payload2["title"]}


def test_get_project_returns_project(client):
    create_response = create_project_via_api(client)

    created_data = create_response.get_json()

    project_id = created_data["id"]

    response = client.get(f"/projects/{project_id}")

    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == project_id
    assert data["title"] == payload["title"]


def test_get_missing_project_returns_404(client):
    response = client.get("/projects/9999")

    data = response.get_json()

    assert response.status_code == 404

    assert data["error"]["code"] == "resource_not_found"
    assert data["error"]["message"] == "Project not found"


def test_update_project_returns_updated_data(client):
    create_response = create_project_via_api(client)

    created_data = create_response.get_json()

    project_id = created_data["id"]

    update_response = client.patch(
        f"/projects/{project_id}", json={**payload, "title": payload2["title"]}
    )

    response = client.get(f"/projects/{project_id}")

    data = response.get_json()

    assert create_response.status_code == 201
    assert update_response.status_code == 200
    assert response.status_code == 200

    assert data["title"] != payload["title"]
    assert data["title"] == payload2["title"]

    assert data["description"] == payload["description"]


def test_update_project_rejects_unknown_fields(client):
    create_response = create_project_via_api(client)

    created_data = create_response.get_json()

    project_id = created_data["id"]

    update_response = client.patch(
        f"/projects/{project_id}",
        json={**payload, "title": payload2["title"], "owner_password": "secret"},
    )

    data = update_response.get_json()

    assert update_response.status_code == 400

    assert data["error"]["code"] == "validation_error"
    assert data["error"]["message"] == "Request validation failed"


def test_delete_project_returns_204(client):
    create_response = client.post("/projects", json=payload)

    created_data = create_response.get_json()

    project_id = created_data["id"]

    delete_response = client.delete(f"/projects/{project_id}")

    assert delete_response.status_code == 204

    get_response = client.get(f"/projects/{project_id}")

    assert get_response.status_code == 404


def test_create_project_without_description_returns_400(client):
    response = client.post(
        "/projects",
        json={
            "title": "project title",
            "github_url": "https://github_url.com",
            "website_url": "https://website_url.com",
        },
    )

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"]["code"] == "validation_error"
    assert data["error"]["message"] == "Request validation failed"


def test_update_project_with_no_fields_returns_400(client):
    create_response = create_project_via_api(client)

    created_response_data = create_response.get_json()
    project_id = created_response_data["id"]

    update_response = client.patch(f"/projects/{project_id}", json={})

    update_response_data = update_response.get_json()

    assert create_response.status_code == 201
    assert update_response.status_code == 400

    assert update_response_data["error"]["code"] == "validation_error"
    assert update_response_data["error"]["message"] == "Request validation failed"


def test_delete_missing_project_returns_404(client):
    response = client.delete("/projects/9999")

    data = response.get_json()

    assert response.status_code == 404
    assert data["error"]["code"] == "resource_not_found"
    assert data["error"]["message"] == "Project not found"


def test_missing_route_returns_HTTPException(client):
    response = client.get("/project/99")
    assert response.status_code == 404
    data = response.get_json()

    assert data == {
        "error": {
            "code": "not_found",
            "message": "The requested URL was not found on the server. "
            "If you entered the URL manually please check your "
            "spelling and try again.",
        }
    }


def test_create_project_reports_multiple_schema_errors(client):
    response = create_project_via_api(
        client, github_url="not-a-url", website_url="not-a-url"
    )

    data = response.get_json()
    assert response.status_code == 400

    details = data["error"]["details"]

    assert "github_url" in details
    assert "website_url" in details


def test_create_project_rejects_invalid_github_url(client):
    response = create_project_via_api(
        client,
        title="Portfolio",
        description="My protfolio",
        github_url="definitely-not-a-url",
    )

    data = response.get_json()

    assert response.status_code == 400
    assert "github_url" in data["error"]["details"]


@patch("app.routes.project.service.get_project")
def test_catches_internal_server_error_for_unknown_operations(mock_get_project, client):
    mock_get_project.side_effect = Exception("Unhandled application error")

    response = client.get("/projects/1")

    data = response.get_json()

    assert response.status_code == 500

    assert data["error"]["code"] == "internal_server_error"
    assert data["error"]["message"] == "An unexpected error occured"


def test_description_accepts_maximum_length(client):
    response = create_project_via_api(client, description="a" * 2000)
    assert response.status_code == 201


def test_description_rejects_above_maximum_length(client):
    response = create_project_via_api(client, description="a" * 2001)

    data = response.get_json()

    assert response.status_code == 400
    assert "description" in data["error"]["details"]


@pytest.mark.parametrize(
    ("length", "expected_status"), [(1999, 201), (2000, 201), (2001, 400)]
)
def test_project_description_length(client, length, expected_status):
    response = create_project_via_api(client, description="a" * length)

    assert response.status_code == expected_status


def test_patch_accepts_single_field(client):
    created = create_project_via_api(client)

    project_id = created.get_json()["id"]

    response = client.patch(f"/projects/{project_id}", json={"description": "updated"})

    assert response.status_code == 200


def test_patch_rejects_empty_object(client):
    response = client.post("/projects", json={})

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"]["code"] == "validation_error"


def test_create_project_rejects_invalid_json(client):
    response = client.post(
        "/projects", data="{'title':", content_type="application/json"
    )

    data = response.get_json()

    assert response.status_code == 400
    assert data["error"]["code"] == "validation_error"
