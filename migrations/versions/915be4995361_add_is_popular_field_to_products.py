"""Add is_popular field to products

Revision ID: 915be4995361
Revises: ec609c27e12a
Create Date: 2025-05-21 06:53:02.986101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '915be4995361'
down_revision = 'ec609c27e12a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_popular', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.drop_column('is_popular')

    # ### end Alembic commands ###
