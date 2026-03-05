from sqlalchemy import Column, Integer, Float
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    from_account = Column(Integer)
    to_account = Column(Integer)
    amount = Column(Float)
