from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.auth import get_db, get_current_user
from src.schemas.article import ArticleCreate
from src.controllers.article_controller import *

router = APIRouter(prefix="/api/articles", tags=["Articles"])


@router.post("", status_code=status.HTTP_201_CREATED)
def create(data: ArticleCreate, user=Depends(get_current_user), db: Session = Depends(get_db)):
    return create_article(data, user.id, db)


@router.get("", status_code=status.HTTP_200_OK)
def list(db: Session = Depends(get_db)):
    return get_articles(db)


@router.get("/{slug}", status_code=status.HTTP_200_OK)
def get(slug: str, db: Session = Depends(get_db)):
    return get_article_by_slug(slug, db)


@router.put("/{slug}", status_code=status.HTTP_200_OK)
def update(slug: str, data: ArticleCreate, user=Depends(get_current_user), db=Depends(get_db)):
    return update_article(slug, data, user.id, db)


@router.delete("/{slug}", status_code=status.HTTP_204_NO_CONTENT)
def delete(slug: str, user=Depends(get_current_user), db=Depends(get_db)):
    delete_article(slug, user.id, db)
