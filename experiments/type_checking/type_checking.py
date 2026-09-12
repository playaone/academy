def format_project_name(
    title: str,
    project_id: int,
) -> str:
    return f"{project_id}: {title}"


name = format_project_name(
    "Engineering Portfolio",
    1
)

print(name)