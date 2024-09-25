"""Added sample and order tables

Revision ID: 6c02f9efc765
Revises: 61b02712e88e
Create Date: 2024-09-25 10:30:27.643008

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c02f9efc765'
down_revision = '61b02712e88e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_orders_uuid'), 'orders', ['uuid'], unique=True)

    op.create_table('samples',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(), nullable=True),
    sa.Column('sequence', sa.String(), nullable=True),
    sa.Column('plate_id', sa.Integer(), nullable=True),
    sa.Column('well', sa.String(length=3), nullable=True),
    sa.Column('qc_1', sa.Float(), nullable=True),
    sa.Column('qc_2', sa.Float(), nullable=True),
    sa.Column('qc_3', sa.Enum('FAIL', 'PASS', name='qcstatus'), nullable=True),
    sa.Column('status', sa.Enum('ORDERED', 'SHIPPED', 'FAILED', name='samplestatus'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_samples_uuid'), 'samples', ['uuid'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_items_title'), table_name='items')
    op.drop_index(op.f('ix_items_description'), table_name='items')
    op.drop_table('items')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_samples_uuid'), table_name='samples')
    op.drop_table('samples')
    op.drop_index(op.f('ix_orders_uuid'), table_name='orders')
    op.drop_table('orders')
