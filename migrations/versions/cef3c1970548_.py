"""empty message

Revision ID: cef3c1970548
Revises: deca9c4b6f7d
Create Date: 2021-04-22 23:02:13.518236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cef3c1970548'
down_revision = 'deca9c4b6f7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('email', sa.String(length=256), nullable=True))
    op.create_unique_constraint(None, 'user_model', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_model', type_='unique')
    op.drop_column('user_model', 'email')
    # ### end Alembic commands ###
