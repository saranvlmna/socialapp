from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from model.connection import engine
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    age = Column(Integer, index=True) 
    password = Column(String, index=True)
Base.metadata.create_all(bind=engine)
