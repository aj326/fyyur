"""switched links to not have uniquness so they can be blank

Revision ID: c2af8464ddfa
Revises: 1609f13093f3
Create Date: 2022-05-30 18:54:32.861538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2af8464ddfa'
down_revision = '1609f13093f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Artist_facebook_link_key', 'Artist', type_='unique')
    op.drop_constraint('Artist_image_link_key', 'Artist', type_='unique')
    op.drop_constraint('Artist_website_key', 'Artist', type_='unique')
    op.drop_constraint('Venue_facebook_link_key', 'Venue', type_='unique')
    op.drop_constraint('Venue_image_link_key', 'Venue', type_='unique')
    op.drop_constraint('Venue_website_key', 'Venue', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('Venue_website_key', 'Venue', ['website'])
    op.create_unique_constraint('Venue_image_link_key', 'Venue', ['image_link'])
    op.create_unique_constraint('Venue_facebook_link_key', 'Venue', ['facebook_link'])
    op.create_unique_constraint('Artist_website_key', 'Artist', ['website'])
    op.create_unique_constraint('Artist_image_link_key', 'Artist', ['image_link'])
    op.create_unique_constraint('Artist_facebook_link_key', 'Artist', ['facebook_link'])
    # ### end Alembic commands ###