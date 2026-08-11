import pytest
from app.repositories.project_repository import ProjectRepository

@pytest.fixture
def repository(app):
    return ProjectRepository()


def test_create_repository(repository):
    project = repository.create(
        title="Engineering Journey",
        description="Backend enginerring project",
        github_url="https://github.com/example/project",
        website_url=None,
        technologies="Flask SQLAlchemy"
    )
    
    assert project.id is not None
    assert project.title == "Engineering Journey"
    assert project.description == "Backend enginerring project"
    

def test_get_by_id(repository):
    created = repository.create(
        title="Project one",
        description="Example"
    )
    
    loaded = repository.get_by_id(created.id)
    
    assert loaded is not None
    assert loaded.id == created.id
    assert loaded.title == "Project one"
    
    
def test_get_by_id_returns_none(repository):
    project = repository.get_by_id(9999)
    
    assert project is None
    
    
def test_update_project(repository):
    project = repository.create(
        title="old",
        description="Old description"
    )
    
    updated = repository.update(
        project,
        title="New",
        description="Updated description"
    )
    
    assert updated.id == project.id
    assert updated.title == "New"
    assert updated.description == "Updated description"
    

def test_delete_project(repository):
    project = repository.create(
        title="Deleted project",
        description="Temporary"
    )
    
    repository.delete(project)
    
    assert repository.get_by_id(project.id) is None
    

def test_get_by_title(repository):
    repository.create(
        title="Portfolio",
        description="Example"
    )
    
    project = repository.get_by_title("Portfolio")
    
    assert project is not None
    assert project.title == "Portfolio"
    

def test_get_by_title_returns_none(repository):
    assert repository.get_by_title("Unknown") is None
    
    
def test_create_sets_timestamps(repository):
    project = repository.create(
        title="Time test",
        description="Testing timestamps"
    )
    
    assert project.created_at is not None
    assert project.updated_at is not None
    
    
def test_update_changed_updated_at(repository):
    import time
    project = repository.create(
        title="Project",
        description="Initial"
    )
    
    original = project.updated_at
    
    time.sleep(0.01)
    
    updated = repository.update(
        project,
        description="changed"
    )
    
    assert updated.updated_at > original
    
    
def test_rollback(repository):
    with pytest.raises(Exception):
        repository.create(...)
        
        
    project = repository.create(
        title="Another Project",
        description="Still works"
    )
    
    assert project.id is not None
    
    
def test_get_all(repository):
    repository.create(
        title="First project",
        description="First project description"
    )
    
    repository.create(
        title="Second Project",
        description="Second project description"
    )
    
    projects = repository.get_all()
    
    assert len(projects) > 0
    assert "First project" in [project.title for project in projects]
    

def test_update_single_field_updates_only_that_field(repository):
    created_project = repository.create(
        title="Created project",
        description="Unchanged Description"
    )
    
    assert created_project.id is not None
    
    updated_project = repository.update(
        created_project,
        description="Changed description"
    )
    
    existing_project = repository.get_by_id(created_project.id)
    
    assert existing_project.id is not None
    
    assert updated_project.title == created_project.title
    assert existing_project.id == created_project.id
    assert existing_project.id == updated_project.id
    
    assert existing_project.title == created_project.title
    assert existing_project.description == updated_project.description
    
    
def test_delete_single_record_does_not_affect_others(repository):
    repository.create(
        title="create something",
        description="Lorem ipsum"
    )
    
    repository.create(
        title="another project",
        description="Another banger"
    )
    
    to_delete = repository.create(
        title="I will be deleted",
        description="I have been deleted"
    )
    
    assert to_delete.id is not None
    
    assert repository.delete(to_delete) is None
    
    projects = repository.get_all()
    
    assert len(projects) > 0
    assert len(projects) >= 2
    

def test_get_all_returns_empty_list_for_fresh_db(repository):
    assert len(repository.get_all()) < 1
    
    