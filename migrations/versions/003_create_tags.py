"""create tags and booktag tables

Revision ID: 003_create_tags
Revises: 002_create_reviews
Create Date: 2026-06-01
"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg
from alembic import op

revision: str = "003_create_tags"
down_revision: Union[str, None] = "002_create_reviews"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tags",
        sa.Column("uid", pg.UUID(as_uuid=True), nullable=False),
        sa.Column("name", pg.VARCHAR(), nullable=False),
        sa.Column("created_at", pg.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint("uid"),
    )

    op.create_table(
        "booktag",
        sa.Column("book_id", pg.UUID(as_uuid=True), nullable=False),
        sa.Column("tag_id", pg.UUID(as_uuid=True), nullable=False),
        sa.ForeignKeyConstraint(["book_id"], ["books.uid"]),
        sa.ForeignKeyConstraint(["tag_id"], ["tags.uid"]),
        sa.PrimaryKeyConstraint("book_id", "tag_id"),
    )


def downgrade() -> None:
    op.drop_table("booktag")
    op.drop_table("tags")
