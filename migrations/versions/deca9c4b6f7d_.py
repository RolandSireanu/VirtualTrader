"""empty message

Revision ID: deca9c4b6f7d
Revises: f5edc22f78bf
Create Date: 2021-04-22 23:01:25.677163

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'deca9c4b6f7d'
down_revision = 'f5edc22f78bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('email', sa.String(length=256), nullable=False))
    op.alter_column('user_model', 'money',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.create_unique_constraint(None, 'user_model', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_model', type_='unique')
    op.alter_column('user_model', 'money',
               existing_type=postgresql.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.drop_column('user_model', 'email')
    # ### end Alembic commands ###
