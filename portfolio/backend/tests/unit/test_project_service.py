import pytest

from app.exceptions import ConflictError, ResourceNotFoundError, ValidationError
from app.services.project_service import ProjectService
from app.repositories.project_repository import ProjectRepository

# class FakeProject:
#     def __init__(
#         self,
#         project_id,
#         title,
#         description,
#         github_url=None,
#         website_url=None,
#     ):
#         self.id = project_id
#         self.title = title
#         self.description = description
#         self.github_url = github_url
#         self.website_url = website_url
        
#     def to_dict(self):
#         return{
#             "id": self.id,
#             "title": self.title,
#             "description": self.description,
#             "github_url": self.github_url,
#             "website_url": self.website_url
#         }
        
        
# class FakeProjectRepository:
#     def __init__(self):
#         self.projects = []
#         self.next_id = 1
        
#     def get_all(self):
#         return list(self.projects)
    
    # def get_by_id(self, project_id):
    #     for project in self.projects:
    #         if project.id == project_id:
    #             return project
            
    #     return None
    
    # def get_by_title(self, title):
    #     for project in self.projects:
    #         if project.title == title:
    #             return project
            
    #     return None
    
    # def create(self, **data):
    #     project = FakeProject(
    #         project_id=self.next_id,
    #         **data
    #     )
        
    #     self.next_id += 1
    #     self.projects.append(project)
        
    #     return project
    
    # def update(self, project, **data):
    #     for field, value in data.items():
    #         setattr(project, field, value)
            
    #     return project
    
    # def delete(self, project):
    #     self.projects.remove(project)
    
@pytest.fixture
def repository(app):
    return ProjectRepository()
        

def test_service_creates_project(repository):
    service = ProjectService(repository)
    
    project = service.create_project(
        {
            "title": "Test Project",
            "description": "Test description"
        }
    )
    
    assert project.id == 1
    assert project.title == "Test Project"
    assert project.description == "Test description"
    
    
# @pytest.mark.parametrize(
#     "title",
#     [
#         None,
#         "",
#         "   ",
#         123
#     ],
# )
# def test_service_rejects_invalid_titles(repository, title):
#     service = ProjectService(repository)
    
#     with pytest.raises(
#         ValidationError,
#         match="Project title is required"
#     ):
#         service.create_project(
#             {
#                 "title": title,
#                 "description": "Valid description"
#             }
#         )
        

def test_service_rejects_duplicate_title(repository):
    service = ProjectService(repository=repository)
    
    service.create_project(
        {
            "title": "Existing project",
            "description": "Test data"
        }
    )
    
    with pytest.raises(
        ConflictError,
        match="A project with this title already exists"
    ):
        service.create_project(
            {
                "title": "Existing project",
                "description": "Test data"
            }
        )
        
        
# def test_service_raises_error_for_missing_project(repository):
#     service = ProjectService(repository)
    
#     with pytest.raises(
#         ResourceNotFoundError,
#         match="Project not found"
#     ):
#         service.get_project(999)
    
    
# @pytest.mark.parametrize("description", [None, 12345, "", "    "])
# def test_service_raises_error_for_invalid_description(repository, description):
#     service = ProjectService(repository)
    
#     with pytest.raises(
#         ValidationError,
#         match="Project description is required"
#     ):
#         service.create_project(
#             {
#                 "title": "Valid Title",
#                 "description": description
#             }
#         )
    

def test_service_update_project_successful(repository):
    service = ProjectService(repository)
    
    created = service.create_project(
        {
            "title": "Create Title",
            "description": "Description for created project"
        }
    )
    
    project_id = created.id
    
    updated = service.update_project(
        project_id,
        {
            "title": "Updated title"
        }
    )
    
    final = service.get_project(project_id)
    
    assert updated.id == project_id
    assert final.title == updated.title
    assert final.description == created.description


def test_service_detetion_successful(repository):
    service = ProjectService(repository)
    
    create_project = service.create_project(
        {
            "title": "Created Project Title",
            "description": "Created Project Description"
        }
    )
    
    project_id = create_project.id
    
    service.delete_project(project_id=project_id)
    
    assert project_id == 1
    
    with pytest.raises(
        ResourceNotFoundError,
        match="Project not found"
    ):
        service.get_project(project_id)
    
    