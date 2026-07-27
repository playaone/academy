from app.exceptions import ConflictError, ResourceNotFoundError, ValidationError, UnsupportedFieldError
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
        title = self._clean_required_text(
            data.get("title"),
            "Project title"
        )
        
        description = self._clean_required_text(
            data.get("description"),
            "Project description"
        )
        
        github_url = self._clean_optional_text(
            data.get("github_url")
        )
        
        website_url = self._clean_optional_text(
            data.get("website_url")
        )
        
        existing_project = self.repository.get_by_title(title)
        
        if existing_project is not None:
            raise ConflictError(
                "A project with this title already exists"
            )
            
        return self.repository.create(
            title=title,
            description=description,
            github_url=github_url,
            website_url=website_url
        )
        
    def update_project(self, project_id, data):
        project = self.get_project(project_id)
        
        updates = {}
        
        data_keys = set(data.keys())
        project_fields = project.to_dict().keys()
        
        unsupported_fields = data_keys - project_fields
        if unsupported_fields:
            raise UnsupportedFieldError(
                f"Unsupported project fields: {', '.join(unsupported_fields)}"
            )
        
        if "title" in data:
            title = self._clean_required_text(
                data.get("title"),
                "Project title"
            )
            
            existing_project = self.repository.get_by_title(title)
            
            if(existing_project is not None and existing_project.id != project.id):
                raise ConflictError(
                    "A project with this title already exists"
                )
                
            updates['title'] = title
            
        if "description" in data:
            updates['description'] = self._clean_required_text(
                data.get("description"),
                "Project description"
            )
        
        if "github_url" in data:
            updates['github_url'] = self._clean_optional_text(
                data.get("github_url")
            )
            
        if "website_url" in data:
            updates['website_url'] = self._clean_optional_text(
                data.get("website_url")
            )
            
        if not updates:
            raise ValidationError(
                "Provide at least one field to update"
            )
            
        return self.repository.update(project, **updates)
    
    def delete_project(self, project_id):
        project = self.get_project(project_id)
        self.repository.delete(project)
        
        
    @staticmethod
    def _clean_required_text(value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise ValidationError(f"{field_name} is required")
        
        return value.strip()
        
    @staticmethod
    def _clean_optional_text(value):
        if value is None:
            return None
        
        if not isinstance(value, str):
            raise ValidationError(
                "Optional text fields must contain text"
            )
            
        clean_value = value.strip()
        
        return clean_value or None