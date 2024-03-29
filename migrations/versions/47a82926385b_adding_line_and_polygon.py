"""adding line and polygon

Revision ID: 47a82926385b
Revises: 397b837e842d
Create Date: 2014-12-06 16:06:58.015927

"""

# revision identifiers, used by Alembic.
revision = '47a82926385b'
down_revision = '397b837e842d'

from alembic import op
import sqlalchemy as sa
import geoalchemy2


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('polygon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('polygon', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=2802), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('line', geoalchemy2.types.Geometry(geometry_type='LINESTRING', srid=32010), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    #op.drop_table('spatial_ref_sys')
    #op.drop_index('idx_POI_point', table_name='POI')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    #op.create_index('idx_POI_point', 'POI', ['point'], unique=False)
    #op.create_table('spatial_ref_sys',
    #sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    #sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    #sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    #sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    #sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    #sa.PrimaryKeyConstraint('srid', name=u'spatial_ref_sys_pkey')
    #)
    op.drop_table('line')
    op.drop_table('polygon')
    ### end Alembic commands ###
