"""add reflection fields

Revision ID: b0c4d1aa8d0d
Revises: c62a7e34e513
Create Date: 2024-04-09 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b0c4d1aa8d0d"
down_revision = "c62a7e34e513"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("question", sa.Column("reflection", sa.Text(), nullable=True))
    op.add_column("practice", sa.Column("reflection", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("practice", "reflection")
    op.drop_column("question", "reflection")
