"""empty message

Revision ID: f5edc22f78bf
Revises: 
Create Date: 2021-04-22 22:51:13.270797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5edc22f78bf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('email', sa.String(length=256), nullable=False))
    op.create_unique_constraint(None, 'user_model', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_model', type_='unique')
    op.drop_column('user_model', 'email')
    # ### end Alembic commands ###