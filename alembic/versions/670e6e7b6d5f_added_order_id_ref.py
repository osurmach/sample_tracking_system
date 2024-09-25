"""Added order id ref

Revision ID: 670e6e7b6d5f
Revises: 3646eb8bab5e
Create Date: 2024-09-25 11:22:30.119772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '670e6e7b6d5f'
down_revision = '3646eb8bab5e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_table('samples')
    op.create_table(
        'samples',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('uuid', sa.String(), nullable=True),
        sa.Column('sequence', sa.String(), nullable=True),
        sa.Column('plate_id', sa.Integer(), nullable=True),
        sa.Column('well', sa.String(length=3), nullable=True),
        sa.Column('qc_1', sa.Float(), nullable=True),
        sa.Column('qc_2', sa.Float(), nullable=True),
        sa.Column('qc_3', sa.Enum('FAIL', 'PASS', name='qcstatus'), nullable=True),
        sa.Column('status', sa.Enum('ORDERED', 'SHIPPED', 'FAILED', name='samplestatus'), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Column('order_id', sa.Integer, sa.ForeignKey('orders.id'))
        )
    op.create_index(op.f('ix_samples_uuid'), 'samples', ['uuid'], unique=True)


def downgrade() -> None:
    pass
