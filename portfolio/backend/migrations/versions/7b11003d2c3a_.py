"""empty message

Revision ID: 7b11003d2c3a
Revises: 8e24b32091bb
Create Date: 2026-07-19 01:55:50.118178

"""

from collections.abc import Sequence

# revision identifiers, used by Alembic.
revision: str = "7b11003d2c3a"
down_revision: str | Sequence[str] | None = "8e24b32091bb"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""


def downgrade() -> None:
    """Downgrade schema."""
