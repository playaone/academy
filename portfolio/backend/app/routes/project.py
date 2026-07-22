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
    try:
        project = service.get_project(project_id)
        return project.to_dict(), 200
    
    except ResourceNotFoundError as error:
        return {"error": str(error)}, 404
    
@projects_bp.post("")
def create_project():
    data = request.get_json(silent=True)
    
    if data is None:
        return{
            "error": "Request body must contain valid JSON"
        }, 400
        
    try:
        project = service.create_project(data)
        return project.to_dict(), 201
    
    except ValidationError as error:
        return {
            "error": str(error)
        }, 404
        
    except ConflictError as error:
        return {
            "error": str(error)
        }, 409
        
@projects_bp.patch("/<int:project_id>")
def update_project(project_id):
    data = request.get_json(silent=True)
    
    if data is None:
        return {
            "error": "Request bosy must contain valid JSON"
        }, 400
        
    try:
        project = service.update_project(project_id, data)
        return project.to_dict(), 200
    
    except ValidationError as error:
        return {
            "error": str(error)
        }, 400
    
    except ResourceNotFoundError as error:
        return {
            "error": str(error)
        }, 404
    
    except ConflictError as error:
        return {
            "error": str(error)
        }, 409
    
@projects_bp.delete("/<int:project_id>")
def delete_project(project_id):
    try:
        service.delete_project(project_id)
        return "", 204
    except ResourceNotFoundError as error:
        return {"error": str(error)}, 404
    
