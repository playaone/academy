from unittest.mock import patch

import pytest
from sqlalchemy.exc import SQLAlchemyError

from app.repositories.project_repository import ProjectRepository
from tests.factories.project_factory import create_project


@pytest.fixture
def repository(app):
    return ProjectRepository()


def test_create_repository(repository):
    project = create_project(
        repository,
        title="Engineering Journey",
        description="Backend enginerring project",
    )

    assert project.id is not None
    assert project.title == "Engineering Journey"
    assert project.description == "Backend enginerring project"


def test_get_by_id(repository):
    created = create_project(repository, title="Project one")

    loaded = repository.get_by_id(created.id)

    assert loaded is not None
    assert loaded.id == created.id
    assert loaded.title == "Project one"


def test_get_by_id_returns_none(repository):
    project = repository.get_by_id(9999)

    assert project is None


def test_update_project(repository):
    project = create_project(repository, title="old", description="Old description")

    updated = repository.update(project, title="New", description="Updated description")

    assert updated.id == project.id
    assert updated.title == "New"
    assert updated.description == "Updated description"


def test_delete_project(repository):
    project = create_project(repository)

    repository.delete(project)

    assert repository.get_by_id(project.id) is None


def test_get_by_title(repository):
    create_project(repository, title="Portfolio", description="Example")

    project = repository.get_by_title("Portfolio")

    assert project is not None
    assert project.title == "Portfolio"


def test_get_by_title_returns_none(repository):
    assert repository.get_by_title("Unknown") is None


def test_create_sets_timestamps(repository):
    project = create_project(
        repository, title="Time test", description="Testing timestamps"
    )

    assert project.created_at is not None
    assert project.updated_at is not None


def test_update_changed_updated_at(repository):
    import time

    project = create_project(repository, description="Initial")

    original = project.updated_at

    time.sleep(0.01)

    updated = repository.update(project, description="changed")

    assert updated.updated_at > original


def test_rollback(repository):
    with pytest.raises(Exception):
        repository.create(...)

    project = create_project(repository)

    assert project.id is not None


def test_get_all(repository):
    create_project(
        repository, title="First project", description="First project description"
    )

    create_project(
        repository, title="Second Project", description="Second project description"
    )

    projects = repository.get_all()

    assert len(projects) > 0
    assert "First project" in [project.title for project in projects]


def test_update_single_field_updates_only_that_field(repository):
    created_project = create_project(repository, description="Unchanged Description")

    assert created_project.id is not None

    updated_project = repository.update(
        created_project, description="Changed description"
    )

    existing_project = repository.get_by_id(created_project.id)

    assert existing_project.id is not None

    assert updated_project.title == created_project.title
    assert existing_project.id == created_project.id
    assert existing_project.id == updated_project.id

    assert existing_project.title == created_project.title
    assert existing_project.description == updated_project.description


def test_delete_single_record_does_not_affect_others(repository):
    create_project(repository, title="create something", description="Lorem ipsum")

    create_project(repository, title="another project", description="Another banger")

    to_delete = create_project(
        repository, title="I will be deleted", description="I have been deleted"
    )

    assert to_delete.id is not None

    assert repository.delete(to_delete) is None

    projects = repository.get_all()

    assert len(projects) > 0
    assert len(projects) >= 2


def test_get_all_returns_empty_list_for_fresh_db(repository):
    assert len(repository.get_all()) < 1


@patch("app.repositories.project_repository.Project")
def test_raises_internal_server_error_for_unknown_operations(
    mock_get_project, repository
):
    mock_get_project.side_effect = Exception("Unhandled application error")

    with pytest.raises(Exception):
        create_project(repository)


@patch("app.repositories.project_repository.db.session.commit")
def test_raises_SQLAlchemyError(mock_db, repository):
    mock_db.side_effect = SQLAlchemyError()

    with pytest.raises(SQLAlchemyError):
        create_project(repository)
