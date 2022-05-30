"""renamed website_link col to website

Revision ID: 1609f13093f3
Revises: a3c2cb8eab0a
Create Date: 2022-05-30 01:11:03.895491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1609f13093f3'
down_revision = 'a3c2cb8eab0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_constraint('Artist_website_link_key', 'Artist', type_='unique')
    op.create_unique_constraint(None, 'Artist', ['website'])
    op.drop_column('Artist', 'website_link')
    op.add_column('Venue', sa.Column('website', sa.String(length=120), nullable=True))
    op.drop_constraint('Venue_website_link_key', 'Venue', type_='unique')
    op.create_unique_constraint(None, 'Venue', ['website'])
    op.drop_column('Venue', 'website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Venue', type_='unique')
    op.create_unique_constraint('Venue_website_link_key', 'Venue', ['website_link'])
    op.drop_column('Venue', 'website')
    op.add_column('Artist', sa.Column('website_link', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Artist', type_='unique')
    op.create_unique_constraint('Artist_website_link_key', 'Artist', ['website_link'])
    op.drop_column('Artist', 'website')
    # ### end Alembic commands ###