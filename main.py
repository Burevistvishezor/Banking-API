from fastapi import FastAPI

from app.database import Base, engine

from app.routers import auth
from app.routers import accounts
from app.routers import transactions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Banking API")

app.include_router(auth.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
