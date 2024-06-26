"""Initial Migration

Revision ID: 39ace67c01a4
Revises: 
Create Date: 2024-05-06 19:37:54.054761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39ace67c01a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('ingredients', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('foods')
    # ### end Alembic commands ###
