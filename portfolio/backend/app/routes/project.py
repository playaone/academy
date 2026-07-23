from flask import Blueprint, request

from app.exceptions import ConflictError, ResourceNotFoundError, ValidationError

from app.services.project_service import ProjectService

projects_bp = Blueprint(
    "projects",
    __name__,
    url_prefix="/projects"
)

service = ProjectService()

@projects_bp.get("")
def list_projects():
    projects = service.list_projects()
    
    return {
        "items": [project.to_dict() for project in projects]
    }, 200
    
@projects_bp.get("/<int:project_id>")
def get_projects(project_id):
    project = service.get_project(project_id)
    return project.to_dict(), 200
    
@projects_bp.post("")
def create_project():
    data = get_json_body()
    
    project = service.create_project(data)
    return project.to_dict(), 201
    
        
@projects_bp.patch("/<int:project_id>")
def update_project(project_id):
    data = get_json_body()
    
    project = service.update_project(project_id, data)
    return project.to_dict(), 200
    
@projects_bp.delete("/<int:project_id>")
def delete_project(project_id):
    service.delete_project(project_id)
    return "", 204

def get_json_body():
    data = request.get_json(silent=True)
    
    if data is None:
        raise ValidationError(
            "Request body must contain valid JSON"
        )
    
    if not isinstance(data, dict):
        raise ValidationError(
            "Request body must be a JSON object"
        )
    
    return data
