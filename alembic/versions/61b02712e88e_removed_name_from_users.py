"""Removed name from users

Revision ID: 61b02712e88e
Revises: 069788063729
Create Date: 2024-09-23 22:12:47.530810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61b02712e88e'
down_revision = '069788063729'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('users', 'name')


def downgrade() -> None:
    op.add_column('users', sa.Column('name', sa.VARCHAR(), nullable=True))
