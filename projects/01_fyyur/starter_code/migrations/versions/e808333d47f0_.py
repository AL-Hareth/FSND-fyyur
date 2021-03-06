"""empty message

Revision ID: e808333d47f0
Revises: cd48ce5b31e3
Create Date: 2020-10-20 14:39:45.684728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e808333d47f0'
down_revision = 'cd48ce5b31e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('genres', sa.PickleType(), nullable=True))
    op.add_column('venue', sa.Column('genres', sa.PickleType(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'genres')
    op.drop_column('artist', 'genres')
    # ### end Alembic commands ###
