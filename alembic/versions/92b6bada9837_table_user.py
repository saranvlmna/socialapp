from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '92b6bada9837'  # Change this to match your file's revision ID
down_revision = None  # Set this to the previous migration if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration: Create users table."""
    op.create_table(
        'users',
        sa.Column('id', sa.Uuid, primary_key=True, default=sa.func.uuid_generate_v4()),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), unique=True, nullable=False),
        sa.Column('age', sa.Numeric(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
    )

def downgrade():
    """Rollback the migration: Drop users table."""
    op.drop_table('users')
