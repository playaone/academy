from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from app.exceptions import ConflictError, ResourceNotFoundError
from app.services.project_service import ProjectService


class FakeProjectRepository:
    def __init__(self):
        self.projects = {}
        self.next_id = 1

    def get_all(self):
        return list(self.projects.values())

    def get_by_id(self, project_id):
        return self.projects.get(project_id)

    def get_by_title(self, project_title):
        for project in self.projects.values():
            if project_title == project.title:
                return project
        return None

    def create(self, **data):
        project = SimpleNamespace(id=self.next_id, **data)

        self.projects[project.id] = project
        self.next_id += 1

        return project

    def update(self, project, **data):
        for field, val in data.items():
            setattr(project, field, val)
        return project

    def delete(self, project):
        del self.projects[project.id]


dummy = {
    "title": "Engineering Journey",
    "description": "Portfolio platform",
    "github_url": None,
    "website_url": None,
    "technologies": "Flask, React",
}


@pytest.fixture()
def repository():
    return FakeProjectRepository()


@pytest.fixture()
def service(repository):
    return ProjectService(repository=repository)


def test_create_project(service):
    project = service.create_project(dummy)

    assert project.id == 1
    assert project.title == dummy["title"]
    assert project.description == dummy["description"]


def test_create_project_rejects_duplicate_title(service):
    service.create_project(dummy)

    with pytest.raises(ConflictError):
        service.create_project(dummy)


def test_duplicate_title_has_correct_message(service):
    service.create_project(dummy)

    with pytest.raises(ConflictError, match="A project with this title already exists"):
        service.create_project(dummy)


def test_get_project_raises_when_missing(service):
    with pytest.raises(ResourceNotFoundError, match="Project not found"):
        service.get_project(999)


def test_get_project(service):
    created = service.create_project(dummy)
    assert created.id is not None

    project = service.get_project(created.id)

    assert project is created


def test_get_project(service):
    created = service.create_project(dummy)

    updated = service.update_project(created.id, {"description": "Updated description"})

    assert updated.title == created.title

    assert updated.description == "Updated description"


def test_update_rejects_title_used_by_another_project(service):
    first = service.create_project({"title": "Portfolio", "description": "First"})

    second = service.create_project({"title": "API Server", "description": "Second"})

    with pytest.raises(ConflictError):
        service.update_project(second.id, {"title": first.title})


def test_project_can_keep_its_existing_title(service):
    project = service.create_project(dummy)

    updated = service.update_project(
        project.id, {"title": dummy["title"], "description": "Updated"}
    )

    assert updated.title == dummy["title"]
    assert updated.description == "Updated"


def test_delete_project(service, repository):
    created = service.create_project(dummy)

    service.delete_project(created.id)

    with pytest.raises(ResourceNotFoundError):
        service.get_project(created.id)

    assert repository.get_by_id(created.id) is None


def test_delete_missing_project_raises(service):
    with pytest.raises(ResourceNotFoundError):
        service.delete_project(999)


@pytest.mark.parametrize("project_id", [100, 999, 5000, 999999])
def test_missing_project_ids_raise(service, project_id):
    with pytest.raises(ResourceNotFoundError):
        service.get_project(project_id)


@pytest.mark.parametrize(
    ("original_title", "new_title"),
    [("Portfolio", "Portfolio"), ("API", "API"), ("Backend", "Backend")],
)
def test_project_can_keep_same_title(service, original_title, new_title):
    project = service.create_project({"title": original_title, "description": "Test"})

    updated = service.update_project(project.id, {"title": new_title})

    assert updated.title == new_title


def test_delete_calls_repository():
    project = SimpleNamespace(id=1)

    repository = Mock()
    repository.get_by_id.return_value = project

    service = ProjectService(repository=repository)

    service.delete_project(1)

    repository.get_by_id.assert_called_once_with(1)
    repository.delete.assert_called_once_with(project)


def test_duplicate_project_does_not_create_record():
    existing = SimpleNamespace(id=1, title="Portfolio")

    repository = Mock()
    repository.get_by_title.return_value = existing

    service = ProjectService(repository=repository)

    with pytest.raises(ConflictError):
        service.create_project({"title": "Portfolio", "description": "Duplicate"})

    repository.create.assert_not_called()
