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

---

## Academy Review

Score:

- Technical correctness: 30/40
- Understanding: 22/30
- Completeness: 15/20
- Engineering practices: 8/10
- Overall: 75/100

What is correct:

- You understand that an ORM maps Python objects/classes to database tables.
- You understand that SQLAlchemy reduces repeated raw SQL.
- You correctly connect `extensions.py` with avoiding circular imports.
- You understand that `db.init_app(app)` supports the application factory pattern.

Corrections:

- ORM means Object-Relational Mapper. It maps classes to tables and object instances to rows.
- SQLAlchemy does not simply "translate Python code into SQL syntax"; it provides model definitions, sessions, queries, relationships, and unit-of-work behavior.
- `extensions.py` usually stores extension instances such as `db = SQLAlchemy()` without binding them to an app immediately.
- The Project mapping answer needs specifics: `__tablename__`, columns, primary key, nullable fields, and Python attributes.

Improved answer:

```text
An ORM maps Python classes to database tables and Python objects to rows, so application code can work with objects while SQLAlchemy handles SQL generation and persistence.

We use SQLAlchemy to avoid scattering raw SQL everywhere, centralize model definitions, use sessions, and keep database access more maintainable.

`extensions.py` stores extension instances such as `db = SQLAlchemy()` so they can be imported without creating circular imports.

We call `db.init_app(app)` because the app is created later by `create_app()`. This keeps the database extension reusable across app instances, including test apps.

The `Project` class maps to the `projects` table. Each `db.Column` defines a table column, `id` is the primary key, and model instances represent rows in that table.
```

Additional practice:

- Explain each column in `app/models/project.py`.
- Write one example of creating a `Project` object and saving it through SQLAlchemy.
