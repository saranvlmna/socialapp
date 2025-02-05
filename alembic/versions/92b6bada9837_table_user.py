from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'unique_revision_id'  # Change this to match your file's revision ID
down_revision = None  # Set this to the previous migration if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration: Create users table."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(50), unique=True, nullable=False),
        sa.Column('email', sa.String(100), unique=True, nullable=False),
        sa.Column('password_hash', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
    )

def downgrade():
    """Rollback the migration: Drop users table."""
    op.drop_table('users')
