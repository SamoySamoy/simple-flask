"""empty message

Revision ID: a08e71570377
Revises: ff307eceba79
Create Date: 2024-05-08 07:02:49.177478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a08e71570377'
down_revision = 'ff307eceba79'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('info', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('book_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('genre', sa.String(), nullable=False),
    sa.Column('published_year', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author_table.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book_table')
    op.drop_table('author_table')
    # ### end Alembic commands ###