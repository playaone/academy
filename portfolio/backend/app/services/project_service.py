from app.exceptions import ConflictError, ResourceNotFoundError
from app.repositories.project_repository import ProjectRepository

class ProjectService:
    def __init__(self, repository=None):
        self.repository = repository or ProjectRepository()
        
        
    def list_projects(self):
        return self.repository.get_all()
    
    
    def get_project(self, project_id):
        project = self.repository.get_by_id(project_id)
        
        if project is None:
            raise ResourceNotFoundError("Project not found")
        
        return project
    
    
    def create_project(self, data):
        
        existing_project = self.repository.get_by_title(data["title"])
        
        if existing_project is not None:
            raise ConflictError(
                "A project with this title already exists"
            )
            
        return self.repository.create(**data)
    
        
    def update_project(self, project_id, data):
        project = self.get_project(project_id)
        
        new_title = data.get('title')
        
        if new_title is not None:
            
            existing_project = self.repository.get_by_title(new_title)
            
            if(existing_project is not None and existing_project.id != project.id):
                raise ConflictError(
                    "A project with this title already exists"
                )
        
            
        return self.repository.update(project, **data)
    
    def delete_project(self, project_id):
        project = self.get_project(project_id)
        self.repository.delete(project)
        
