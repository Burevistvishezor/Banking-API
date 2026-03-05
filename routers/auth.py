from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    hashed = bcrypt.hash(user.password)

    db_user = User(
        email=user.email,
        password=hashed
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "user created"}
