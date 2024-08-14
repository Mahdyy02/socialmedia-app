"""add content column to posts table

Revision ID: be4a2d177971
Revises: ebfd2e1206fe
Create Date: 2024-08-14 12:20:27.756186

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be4a2d177971'
down_revision: Union[str, None] = 'ebfd2e1206fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
