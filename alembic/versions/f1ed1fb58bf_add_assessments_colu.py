"""add assessments column

Revision ID: f1ed1fb58bf
Revises: 10cb6c607a43
Create Date: 2013-08-29 22:39:51.217153

"""

# revision identifiers, used by Alembic.
revision = 'f1ed1fb58bf'
down_revision = '10cb6c607a43'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('registrations', sa.Column('assessments', sa.Boolean))


def downgrade():
    op.drop_column('registrations', 'assessments')
