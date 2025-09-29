"""remove probabilities and reflection fields

Revision ID: a2f4d9c1a7b6
Revises: e8b7c6a5d4f3
Create Date: 2025-09-26 00:05:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a2f4d9c1a7b6"
down_revision = "e8b7c6a5d4f3"
branch_labels = None
depends_on = None


def upgrade():
    # Drop from question
    with op.batch_alter_table("question") as batch_op:
        try:
            batch_op.drop_column("criterion_probabilities")
        except Exception:
            pass
        try:
            batch_op.drop_column("pass_probability")
        except Exception:
            pass
        try:
            batch_op.drop_column("reflection")
        except Exception:
            pass

    # Drop from practice
    with op.batch_alter_table("practice") as batch_op:
        try:
            batch_op.drop_column("criterion_probabilities")
        except Exception:
            pass
        try:
            batch_op.drop_column("pass_probability")
        except Exception:
            pass
        try:
            batch_op.drop_column("reflection")
        except Exception:
            pass


def downgrade():
    # Re-add to question
    with op.batch_alter_table("question") as batch_op:
        batch_op.add_column(sa.Column("reflection", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("pass_probability", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("criterion_probabilities", sa.Text(), nullable=True))

    # Re-add to practice
    with op.batch_alter_table("practice") as batch_op:
        batch_op.add_column(sa.Column("reflection", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("pass_probability", sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column("criterion_probabilities", sa.Text(), nullable=True))

