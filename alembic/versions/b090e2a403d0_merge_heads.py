"""merge heads

Revision ID: b090e2a403d0
Revises: 6fa2c63fa5b6, bd30cc6e0449
Create Date: 2026-07-14 20:39:57.213856

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b090e2a403d0'
down_revision: Union[str, Sequence[str], None] = ('6fa2c63fa5b6', 'bd30cc6e0449')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
