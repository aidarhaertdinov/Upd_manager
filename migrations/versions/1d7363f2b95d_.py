"""empty message

Revision ID: 1d7363f2b95d
Revises: 
Create Date: 2022-10-28 18:33:26.107993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d7363f2b95d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id_order', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('date', sa.Text(), nullable=True),
    sa.Column('seller', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id_order')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(length=70), nullable=True),
    sa.Column('password', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name')
    )
    op.create_table('product_line',
    sa.Column('id_product_line', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=100), nullable=True),
    sa.Column('unit_of_measurement', sa.String(length=10), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('cost_without_tax', sa.Float(), nullable=True),
    sa.Column('tax_rate', sa.Integer(), nullable=True),
    sa.Column('tax_amount', sa.Float(), nullable=True),
    sa.Column('cost_with_tax', sa.Float(), nullable=True),
    sa.Column('id_order', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_order'], ['order.id_order'], ),
    sa.PrimaryKeyConstraint('id_product_line')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_line')
    op.drop_table('users')
    op.drop_table('order')
    # ### end Alembic commands ###
