from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from src.models.comment import Comment
from src.models.article import Article


def add_comment(slug: str, data, db: Session):
    article = db.query(Article).filter_by(slug=slug).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Article not found")

    comment = Comment(body=data.body, article_id=article.id)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment


def get_comments(slug: str, db: Session):
    article = db.query(Article).filter_by(slug=slug).first()
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Article not found")

    return db.query(Comment).filter_by(article_id=article.id).all()


def delete_comment(comment_id: int, db: Session):
    comment = db.query(Comment).filter_by(id=comment_id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Comment not found")

    db.delete(comment)
    db.commit()
