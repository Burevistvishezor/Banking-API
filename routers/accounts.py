from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.account import Account
from app.schemas.account import AccountCreate

router = APIRouter(prefix="/accounts")

@router.post("/")
def create_account(account: AccountCreate, db: Session = Depends(get_db)):

    db_account = Account(
        user_id=account.user_id,
        balance=0
    )

    db.add(db_account)
    db.commit()
    db.refresh(db_account)

    return db_account


@router.get("/")
def get_accounts(db: Session = Depends(get_db)):
    return db.query(Account).all()
