from app.extensions import db
from datetime import datetime

class Project(db.Model):
    __tablename__ = "projects"
    
    id = db.Column(db.Integer, primary_key=True)
    
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    github_url = db.Column(db.String(255), nullable=True)
    website_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "github_url": self.github_url,
            "website_url": self.website_url,
            "created_at": (
                self.created_at.isoformat()
                if self.created_at 
               else None
            ),
            "updated_at": (
                self.updated_at.isoformat()
                if self.updated_at
                else None
            )
        }
        
