from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    bio: Optional[str] = None
    image_url: Optional[str] = None


class UserPublic(BaseModel):
    id: int
    email: EmailStr
    username: str
    bio: Optional[str]
    image_url: Optional[str]

    class Config:
        orm_mode = True
