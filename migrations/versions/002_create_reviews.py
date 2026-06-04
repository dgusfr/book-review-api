"""create reviews table

Revision ID: 002_create_reviews
Revises: 001_create_users_and_books
Create Date: 2026-06-01
"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg
from alembic import op

revision: str = "002_create_reviews"
down_revision: Union[str, None] = "001_create_users_and_books"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "reviews",
        sa.Column("uid", pg.UUID(as_uuid=True), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=False),
        sa.Column("review_text", pg.VARCHAR(), nullable=False),
        sa.Column("user_uid", pg.UUID(as_uuid=True), nullable=True),
        sa.Column("book_uid", pg.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", pg.TIMESTAMP(), nullable=True),
        sa.Column("update_at", pg.TIMESTAMP(), nullable=True),
        sa.ForeignKeyConstraint(["book_uid"], ["books.uid"]),
        sa.ForeignKeyConstraint(["user_uid"], ["users.uid"]),
        sa.PrimaryKeyConstraint("uid"),
    )


def downgrade() -> None:
    op.drop_table("reviews")
