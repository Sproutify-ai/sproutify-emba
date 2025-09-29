"""add per-criterion justifications

Revision ID: e8b7c6a5d4f3
Revises: df4c2f5f6f39
Create Date: 2025-09-26 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e8b7c6a5d4f3"
down_revision = "df4c2f5f6f39"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("question", sa.Column("criterion_justifications", sa.Text(), nullable=True))
    op.add_column("practice", sa.Column("criterion_justifications", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("practice", "criterion_justifications")
    op.drop_column("question", "criterion_justifications")

