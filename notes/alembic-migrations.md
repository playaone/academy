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