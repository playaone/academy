from flask import Blueprint, request

from app.exceptions import ValidationError
from app.schemas.project_schema import (
    project_create_schema,
    project_response_schema,
    project_update_schema,
    projects_response_schema,
)
from app.services.project_service import ProjectService

projects_bp = Blueprint("projects", __name__, url_prefix="/projects")

service = ProjectService()


@projects_bp.get("")
def list_projects():
    projects = service.list_projects()

    return {"items": projects_response_schema.dump(projects)}, 200


@projects_bp.get("/<int:project_id>")
def get_projects(project_id):
    project = service.get_project(project_id)

    return project_response_schema.dump(project), 200


@projects_bp.post("")
def create_project():
    data = get_json_body()

    validated_data = project_create_schema.load(data)

    project = service.create_project(validated_data)

    return project_response_schema.dump(project), 201


@projects_bp.patch("/<int:project_id>")
def update_project(project_id):
    data = get_json_body()

    validated_data = project_update_schema.load(data)

    project = service.update_project(project_id, validated_data)

    return project_response_schema.dump(project), 200


@projects_bp.delete("/<int:project_id>")
def delete_project(project_id):
    service.delete_project(project_id)
    return "", 204


def get_json_body():
    data = request.get_json(silent=True)

    if data is None:
        raise ValidationError("Request body must contain valid JSON")

    if not isinstance(data, dict):
        raise ValidationError("Request body must be a JSON object")

    return data
