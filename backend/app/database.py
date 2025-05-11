from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from app.config import settings

# MySQL 엔진 생성
# 참고: 사용된 DATABASE_URL은 동기식이지만, 필요에 따라 asyncio 지원 드라이버로 변경 가능합니다
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=True,
)

# 세션 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 모델의 기본 클래스
Base = declarative_base()

def get_db():
    """DB 세션 의존성"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 