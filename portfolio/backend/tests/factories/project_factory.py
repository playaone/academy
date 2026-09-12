def build_project_data(*, sequence=None, **overrides):
    suffix = f" {sequence}" if sequence is not None else ""
    data = {
        "title": f"Engineering Journey Platform{suffix}",
        "description": "A full-stack portfolio platform",
        "github_url": None,
        "website_url": None,
        "technologies": None,
    }

    data.update(overrides)

    return data


def create_project_via_api(client, **overrides):
    payload = build_project_data(**overrides)

    response = client.post("/projects", json=payload)

    return response


def create_project(repository, **overrides):
    data = build_project_data(**overrides)
    return repository.create(**data)
