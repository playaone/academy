Why are migrations better than manually editing a database?
    Migrations will help you keep track of changes made to the database.

What does alembic revision --autogenerate do?
    This compares the current state of your database and the changes you are about to make, then it generates a revision file that will be used to apply the changes.

Why should you review generated migrations before applying them?
    To make sure the generated migration reflects what you have in mind.

What is the purpose of the alembic_version table?
    This tracks the migrations applied to the database.

What is the difference between:
upgrade
    Upgrade runs when a newer migration is applied to the database.
downgrade
    Downgrade runs when the Alembic needs to apply a previous migration.

---

## Academy Review

Score:

- Technical correctness: 33/40
- Understanding: 25/30
- Completeness: 17/20
- Engineering practices: 8/10
- Overall: 83/100

What is correct:

- You understand that migrations track database schema changes over time.
- You correctly identify `alembic_version` as the table that records the applied migration revision.
- You correctly describe `upgrade` as moving the database forward.

Corrections:

- `alembic revision --autogenerate` compares SQLAlchemy model metadata against the current database schema, then creates a migration script. It does not compare against "changes you are about to make" in a general sense.
- Reviewing generated migrations matters because autogenerate can miss intent, produce unsafe operations, or generate changes that need manual adjustment.
- `downgrade` is not just "when Alembic needs a previous migration"; it is the function that reverses the schema changes from a migration.

Improved answer:

```text
Migrations are better than manual edits because they make schema changes repeatable, reviewable, version-controlled, and shareable across development, testing, and production environments.

`alembic revision --autogenerate` compares the current database schema with SQLAlchemy model metadata and creates a migration file for the detected schema differences.

Generated migrations should be reviewed because Alembic can detect structure, but it cannot always know developer intent or data-safety concerns.

The `alembic_version` table stores the current applied migration revision.

`upgrade` applies a migration forward. `downgrade` reverses that migration.
```

Additional practice:

- Open each migration file and explain what its `upgrade()` and `downgrade()` do.
- Create a model change locally, run autogenerate, and inspect the migration before applying it.
