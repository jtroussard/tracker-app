"""empty message

Revision ID: 5127776ebf69
Revises: 
Create Date: 2023-05-08 01:45:24.894489

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5127776ebf69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('middle_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('image_file', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('joined_date', sa.DateTime(), nullable=False),
    sa.Column('active_record', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('time_of_day', sa.String(length=20), nullable=True),
    sa.Column('mood', sa.String(length=20), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=True),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('measurement_waist', sa.Float(), nullable=True),
    sa.Column('keto', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('active_record', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['member.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('entry')
    op.drop_table('member')
    # ### end Alembic commands ###
