"""followers

Revision ID: 7067ceb51a0f
Revises: 8c3207e83e36
Create Date: 2021-01-04 19:16:31.911172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7067ceb51a0f'
down_revision = '8c3207e83e36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
