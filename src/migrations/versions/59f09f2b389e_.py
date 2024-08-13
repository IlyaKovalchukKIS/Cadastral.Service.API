"""empty message

Revision ID: 59f09f2b389e
Revises: 
Create Date: 2024-08-09 18:01:43.434486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59f09f2b389e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cadastral',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cadaster_number', sa.String(), nullable=False),
    sa.Column('longitude', sa.String(), nullable=False),
    sa.Column('width', sa.String(), nullable=False),
    sa.Column('date_at', sa.DateTime(), nullable=False),
    sa.Column('result', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cadastral')
    # ### end Alembic commands ###