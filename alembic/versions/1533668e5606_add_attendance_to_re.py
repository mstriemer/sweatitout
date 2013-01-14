"""add attendance to Registration

Revision ID: 1533668e5606
Revises: None
Create Date: 2013-01-13 21:11:11.661970

"""

# revision identifiers, used by Alembic.
revision = '1533668e5606'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('registrations', sa.Column('attendance', sa.String(25), nullable=False, server_default='both'))

def downgrade():
    op.drop_column('registrations', 'attendance')
