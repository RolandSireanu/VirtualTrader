"""empty message

Revision ID: dd496397ca92
Revises: 
Create Date: 2021-03-30 21:14:22.278936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd496397ca92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction_model', sa.Column('price', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transaction_model', 'price')
    # ### end Alembic commands ###
