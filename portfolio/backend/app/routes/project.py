from flask import Blueprint

from app.repositories.project_repository import ProjectRepository

projects_bp = Blueprint("projects", __name__)

repository = ProjectRepository()

@projects_bp.get("/projects")
def list_projects():
    projects = repository.get_all()
    
    return [project.to_dict() for project in projects]

@projects_bp.get("/project/search/<str:title>")
def get_by_title(title):
    project = repository.get_by_title(title=title)
    return project