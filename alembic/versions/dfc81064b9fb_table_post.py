from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = 'dfc81064b9fb'  # Change this to match your file's revision ID
down_revision = None  # Set this to the previous migration if applicable
branch_labels = None
depends_on = None

def upgrade():
    """Apply the migration: Create posts table."""
    op.create_table(
        'posts',
        sa.Column('id', sa.Uuid, primary_key=True, default=sa.func.uuid_generate_v4()),
        sa.Column('user_id', sa.String(), unique=True, nullable=False),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('discription', sa.String(), nullable=False),
        sa.Column('url', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()),
    )

def downgrade():
    """Rollback the migration: Drop posts table."""
    op.drop_table('posts')
