from __future__ import with_statement

import logging
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import your Base object from your models.py in the app directory
from app.models import Base  # Adjusted to point to app/models.py

# Interpret the config file for Python logging.
# This line sets up loggers.
fileConfig(context.config.config_file_name)
logger = logging.getLogger('alembic.env')

# Add your model's MetaData object here
target_metadata = Base.metadata

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        context.config.get_section(context.config.config_ini_section),
        prefix='sqlalchemy.', poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            # Other options can go here as needed
        )

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = context.config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()

# Choose between online and offline mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()