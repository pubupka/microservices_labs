from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.schemas.user import *
from src.auth import get_db, get_current_user
from src.controllers.user_controller import create_user, login_user

router = APIRouter(prefix="/api", tags=["Users"])


@router.post("/users", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)


@router.post("/users/login", status_code=status.HTTP_200_OK)
def login(data: UserLogin, db: Session = Depends(get_db)):
    token = login_user(data, db)
    return {"token": token}


@router.get("/user", status_code=status.HTTP_200_OK)
def get_user(current=Depends(get_current_user)):
    return current


@router.put("/user", status_code=status.HTTP_200_OK)
def update_user(update: UserUpdate, current=Depends(get_current_user), db: Session = Depends(get_db)):
    for k, v in update.dict(exclude_none=True).items():
        setattr(current, k, v)
    db.commit()
    return current
