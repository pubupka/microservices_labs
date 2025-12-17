from sqlalchemy import Column, Integer, String, Text, ForeignKey
from src.db import Base


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    body = Column(Text)
    slug = Column(String, unique=True, index=True)
    tags = Column(String)
    author_id = Column(Integer, ForeignKey("users.id"))