"""Added account table

Revision ID: 069788063729
Revises: cc466880d6e4
Create Date: 2024-09-21 22:27:44.892097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '069788063729'
down_revision = 'cc466880d6e4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column('items', 'version')
    op.add_column('users', sa.Column('name', sa.String))


def downgrade() -> None:
    op.drop_column('users', 'name')
    op.add_column('items', sa.Column('version', sa.String))
