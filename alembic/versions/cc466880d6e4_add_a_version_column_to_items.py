"""Add a version column to items

Revision ID: cc466880d6e4
Revises: ddb65078eb5f
Create Date: 2024-09-21 13:36:11.499481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc466880d6e4'
down_revision = 'ddb65078eb5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('items', sa.Column('version', sa.String))


def downgrade() -> None:
    op.drop_column('items', 'version')
