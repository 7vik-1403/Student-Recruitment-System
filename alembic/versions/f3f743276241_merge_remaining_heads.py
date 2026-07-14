"""merge remaining heads

Revision ID: f3f743276241
Revises: 8a343a4cc482, b090e2a403d0
Create Date: 2026-07-14 20:44:22.504943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3f743276241'
down_revision: Union[str, Sequence[str], None] = ('8a343a4cc482', 'b090e2a403d0')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
