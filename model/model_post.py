from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from model.connection import engine
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'posts'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True))
    title = Column(String, unique=True, index=True)
    discription = Column(String, unique=True, index=True)
    url = Column(String, index=True) 

Base.metadata.create_all(bind=engine)

