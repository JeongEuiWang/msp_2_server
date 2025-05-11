from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.database import Base

class Event(Base):

    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    organizer = Column(String(100), nullable=False)
    month = Column(Integer, nullable=False)
    registration_period = Column(String(100), nullable=True)
    link = Column(String(500), nullable=True)
    category_json = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now()) 
