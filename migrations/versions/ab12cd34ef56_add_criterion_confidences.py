"""add criterion confidences per criterion

Revision ID: ab12cd34ef56
Revises: a2f4d9c1a7b6
Create Date: 2025-09-27 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ab12cd34ef56"
down_revision = "a2f4d9c1a7b6"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("question", sa.Column("criterion_confidences", sa.Text(), nullable=True))
    op.add_column("practice", sa.Column("criterion_confidences", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("practice", "criterion_confidences")
    op.drop_column("question", "criterion_confidences")

