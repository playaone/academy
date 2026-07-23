from sqlalchemy.exc import SQLAlchemyError

from app.extensions import db
from app.models.project import Project

class ProjectRepository:
    def get_all(self):
        return Project.query.order_by(
            Project.created_at.desc()
        ).all()
    
    def get_by_id(self, project_id):
        return db.session.get(Project, project_id)
    
    def get_by_title(self, title):
        return Project.query.filter_by(title=title).first()
    
    def create(self, **data):
        project = Project(**data)
        
        try:        
            db.session.add(project)
            db.session.commit()
            db.session.refresh(project)
            
            return project
        
        except SQLAlchemyError:
            db.session.rollback()
            raise
    
    def update(self, project, **data):
        try:
            for field, value in data.items():
                setattr(project, field, value)
            
            db.session.commit()
            db.session.refresh(project)
            
            return project
        except SQLAlchemyError:
            db.session.rollback()
            raise
    
    def delete(self, project):
        try:
            db.session.delete(project)
            db.session.commit()
            
        except SQLAlchemyError:
            db.session.rollback()
            raise