from sqlalchemy import Column, Integer, String
from src.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    bio = Column(String, nullable=True)
    image_url = Column(String, nullable=True)