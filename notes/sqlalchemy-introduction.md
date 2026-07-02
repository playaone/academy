Answer these questions:

What problem does an ORM solve?
    ORM maps object to database models.

Why are we using SQLAlchemy instead of writing raw SQL everywhere?
    SQLALCHEMY translates python codes into SQL syntax so we don't have to write long repetitive SQL.

What is the responsibility of extensions.py?
    extensions.py organizes dependencies/extensions in one file to initialize them and prevent circular imports.

Why do we call db.init_app(app) instead of creating SQLAlchemy(app) directly?
    db is an instance of the SQLalchemy and the init_app() method attaches the instance to the application, this keeps it reusable while avoiding circular imports.

Explain how the Project class maps to a database table.
    A Project class maps to a database through SQLAlchemy automatically.