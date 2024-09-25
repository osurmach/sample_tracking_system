"""Cahnged uuid field

Revision ID: 3f155fbdfd26
Revises: 32775e60ffe3
Create Date: 2024-09-25 12:23:28.206853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f155fbdfd26'
down_revision = '32775e60ffe3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('orders', sa.Column('order_uuid', sa.String(), nullable=True))
    op.drop_index('ix_orders_uuid', table_name='orders')
    op.create_index(op.f('ix_orders_order_uuid'), 'orders', ['order_uuid'], unique=True)
    op.drop_column('orders', 'uuid')
    op.add_column('samples', sa.Column('sample_uuid', sa.String(), nullable=True))
    op.drop_index('ix_samples_uuid', table_name='samples')
    op.create_index(op.f('ix_samples_sample_uuid'), 'samples', ['sample_uuid'], unique=True)
    op.drop_column('samples', 'uuid')


def downgrade() -> None:
    op.add_column('samples', sa.Column('uuid', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_samples_sample_uuid'), table_name='samples')
    op.create_index('ix_samples_uuid', 'samples', ['uuid'], unique=False)
    op.drop_column('samples', 'sample_uuid')
    op.add_column('orders', sa.Column('uuid', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_orders_order_uuid'), table_name='orders')
    op.create_index('ix_orders_uuid', 'orders', ['uuid'], unique=False)
    op.drop_column('orders', 'order_uuid')
