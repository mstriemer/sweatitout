"""create_program_design_registration_table

Revision ID: 409390a3a848
Revises: f1ed1fb58bf
Create Date: 2015-05-04 22:14:17.704302

"""

# revision identifiers, used by Alembic.
revision = '409390a3a848'
down_revision = 'f1ed1fb58bf'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'program_design_registration',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('trainer', sa.String(255), nullable=False),
        sa.Column('package', sa.String(255), nullable=False),
        sa.Column('registration_date', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('program_design_registration')
