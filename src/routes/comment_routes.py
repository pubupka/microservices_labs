from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.auth import get_db, get_current_user
from src.schemas.comment import CommentCreate
from src.controllers.comment_controller import *

router = APIRouter(prefix="/api/articles", tags=["Comments"])


@router.post("/{slug}/comments", status_code=status.HTTP_201_CREATED)
def add(slug: str, data: CommentCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    return add_comment(slug, data, db)


@router.get("/{slug}/comments", status_code=status.HTTP_200_OK)
def list(slug: str, db: Session = Depends(get_db)):
    return get_comments(slug, db)


@router.delete("/{slug}/comments/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(slug: str, id: int, user=Depends(get_current_user), db: Session = Depends(get_db)):
    delete_comment(id, db)
