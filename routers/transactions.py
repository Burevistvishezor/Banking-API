from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.account import Account
from app.models.transaction import Transaction
from app.schemas.transaction import Transfer

router = APIRouter(prefix="/transactions")

@router.post("/transfer")
def transfer(data: Transfer, db: Session = Depends(get_db)):

    from_acc = db.query(Account).filter(Account.id == data.from_account).first()
    to_acc = db.query(Account).filter(Account.id == data.to_account).first()

    if from_acc.balance < data.amount:
        return {"error": "not enough money"}

    from_acc.balance -= data.amount
    to_acc.balance += data.amount

    transaction = Transaction(
        from_account=data.from_account,
        to_account=data.to_account,
        amount=data.amount
    )

    db.add(transaction)
    db.commit()

    return {"message": "transfer successful"}
