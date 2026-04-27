"""Create phone number for user column

Revision ID: 304b6374bea2
Revises: 
Create Date: 2026-04-28 03:08:23.639812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '304b6374bea2'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    op.execute("ALTER TABLE users DROP COLUMN IF EXISTS phone_number")
