from app.extensions import db
from app.models.project import Project

class ProjectRepository:
    def get_all(self):
        return Project.query.all()
    
    def get_by_id(self, project_id):
        return db.session.get(Project, project_id)
    
    def create(self, **data):
        project = Project(**data)
        
        db.session.add(project)
        db.session.commit()
        
        return project
    
    def delete(self, project):
        db.session.delete(project)
        db.session.commit()
        
    def get_by_title(self, title):
        project = Project.query.filter_by(title=title).first()
        return project
    
    def update(self, project, **data):
        for field, value in data.items():
            setattr(project, field, value)
        
        db.session.commit()
        db.session.refresh(project)
        
        return project