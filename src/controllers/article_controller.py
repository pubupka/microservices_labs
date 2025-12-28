from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.article import Article
from slugify import slugify
import json


def create_article(data, user_id: int, db: Session):
    slug = slugify(data.title)

    article = Article(
        title=data.title,
        description=data.description,
        body=data.body,
        slug=slug,
        tags=json.dumps(data.tagList),
        author_id=user_id
    )

    db.add(article)
    db.commit()
    db.refresh(article)
    return article


def get_articles(db: Session):
    return db.query(Article).all()


def get_article_by_slug(slug: str, db: Session):
    article = db.query(Article).filter_by(slug=slug).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return article


def update_article(slug: str, data, user_id: int, db: Session):
    article = db.query(Article).filter_by(slug=slug, author_id=user_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Article not found or no permission")

    article.title = data.title
    article.description = data.description
    article.body = data.body
    article.tags = json.dumps(data.tagList)

    db.commit()
    db.refresh(article)
    return article


def delete_article(slug: str, user_id: int, db: Session):
    article = db.query(Article).filter_by(slug=slug, author_id=user_id).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Article not found or no permission")

    db.delete(article)
    db.commit()
