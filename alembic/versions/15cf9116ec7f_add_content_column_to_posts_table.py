"""add content column to posts table

Revision ID: 15cf9116ec7f
Revises: b88c003b6837
Create Date: 2023-12-10 21:23:17.848600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15cf9116ec7f'
down_revision: Union[str, None] = 'b88c003b6837'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
