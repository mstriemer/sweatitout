"""Add referrer_name to registration

Revision ID: 10cb6c607a43
Revises: 1533668e5606
Create Date: 2013-06-18 21:59:45.239377

"""

# revision identifiers, used by Alembic.
revision = '10cb6c607a43'
down_revision = '1533668e5606'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('registrations', sa.Column('referrer_name', sa.String(255)))


def downgrade():
    op.drop_column('registrations', 'referrer_name')
