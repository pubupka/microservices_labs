from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.user import User
from src.auth import hash_password, verify_password
from src.auth import create_token

def create_user(data, db: Session):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(400, "Email already registered")

    user = User(email=data.email, username=data.username, password=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(data, db: Session):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(400, "Invalid credentials")
    return create_token({"id": user.id})
