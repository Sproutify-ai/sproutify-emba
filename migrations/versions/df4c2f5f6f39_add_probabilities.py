"""add probabilities

Revision ID: df4c2f5f6f39
Revises: b0c4d1aa8d0d
Create Date: 2024-04-09 00:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "df4c2f5f6f39"
down_revision = "b0c4d1aa8d0d"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("question", sa.Column("pass_probability", sa.Integer(), nullable=True))
    op.add_column("question", sa.Column("criterion_probabilities", sa.Text(), nullable=True))
    op.add_column("practice", sa.Column("pass_probability", sa.Integer(), nullable=True))
    op.add_column("practice", sa.Column("criterion_probabilities", sa.Text(), nullable=True))


def downgrade():
    op.drop_column("practice", "criterion_probabilities")
    op.drop_column("practice", "pass_probability")
    op.drop_column("question", "criterion_probabilities")
    op.drop_column("question", "pass_probability")
