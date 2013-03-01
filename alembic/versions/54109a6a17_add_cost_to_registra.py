"""add cost to registration

Revision ID: 54109a6a17
Revises: 1533668e5606
Create Date: 2013-02-28 20:37:29.684063

"""

# revision identifiers, used by Alembic.
revision = '54109a6a17'
down_revision = '1533668e5606'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('registrations', sa.Column('cost', sa.Integer))


def downgrade():
    op.drop_column('registrations', 'cost')
