from pydantic import BaseModel


class CommentCreate(BaseModel):
    body: str


class CommentPublic(BaseModel):
    id: int
    body: str
    article_id: int

    class Config:
        orm_mode = True
