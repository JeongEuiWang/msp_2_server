from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy import engine_from_config

from alembic import context

# 로컬 모델 가져오기
from app.database import Base
from app.models import *  # 모든 모델 가져오기
from app.config import settings  # DB URL 설정 가져오기

# Alembic이 이 파일을 로드하도록 설정
config = context.config

# Alembic 로깅 설정 해석
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 메타데이터 객체 추가 - 모델에서 설정한 내용대로 반영
target_metadata = Base.metadata

# 다른 값들은 설정대로 사용
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online() 