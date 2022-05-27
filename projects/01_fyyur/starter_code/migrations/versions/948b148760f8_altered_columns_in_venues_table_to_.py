"""altered columns in venues table to account for nullibality and uniqueness

Revision ID: 948b148760f8
Revises: bc21190245fb
Create Date: 2022-05-27 17:41:14.350012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '948b148760f8'
down_revision = 'bc21190245fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Venue', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Venue', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Venue', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Venue', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Venue', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('Venue', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Venue', 'website',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('Venue', 'seeking_description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.create_unique_constraint(None, 'Venue', ['facebook_link'])
    op.create_unique_constraint(None, 'Venue', ['website'])
    op.create_unique_constraint(None, 'Venue', ['name'])
    op.create_unique_constraint(None, 'Venue', ['seeking_description'])
    op.create_unique_constraint(None, 'Venue', ['phone'])
    op.create_unique_constraint(None, 'Venue', ['image_link'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Venue', type_='unique')
    op.drop_constraint(None, 'Venue', type_='unique')
    op.alter_column('Venue', 'seeking_description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Venue', 'seeking_talent',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('Venue', 'genres',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('Venue', 'website',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('Venue', 'phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Venue', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
