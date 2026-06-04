"""create users and books tables

Revision ID: 001_create_users_and_books
Revises: None
Create Date: 2026-06-01
"""

from typing import Sequence, Union

import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg
from alembic import op

revision: str = "001_create_users_and_books"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("uid", pg.UUID(as_uuid=True), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("role", pg.VARCHAR(), server_default="user", nullable=False),
        sa.Column(
            "is_verified", sa.Boolean(), nullable=False, server_default=sa.text("false")
        ),
        sa.Column("password_hash", pg.VARCHAR(), nullable=False),
        sa.Column("created_at", pg.TIMESTAMP(), nullable=True),
        sa.Column("update_at", pg.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint("uid"),
    )

    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "books",
        sa.Column("uid", pg.UUID(as_uuid=True), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("author", sa.String(), nullable=False),
        sa.Column("publisher", sa.String(), nullable=False),
        sa.Column("published_date", sa.Date(), nullable=False),
        sa.Column("page_count", sa.Integer(), nullable=False),
        sa.Column("language", sa.String(), nullable=False),
        sa.Column("user_uid", pg.UUID(as_uuid=True), nullable=True),
        sa.Column("created_at", pg.TIMESTAMP(), nullable=True),
        sa.Column("update_at", pg.TIMESTAMP(), nullable=True),
        sa.ForeignKeyConstraint(["user_uid"], ["users.uid"]),
        sa.PrimaryKeyConstraint("uid"),
    )


def downgrade() -> None:
    op.drop_table("books")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
