from sqlalchemy import Column, Integer, Text, ForeignKey
from src.db import Base


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    body = Column(Text)
    article_id = Column(Integer, ForeignKey("articles.id"))