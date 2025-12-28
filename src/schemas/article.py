from pydantic import BaseModel
from typing import List, Optional

class ArticleBase(BaseModel):
    title: str
    description: str
    body: str
    tagList: Optional[List[str]] = []


class ArticleCreate(ArticleBase):
    pass


class ArticlePublic(ArticleBase):
    id: int
    slug: str
    author_id: int

    class Config:
        orm_mode = True
