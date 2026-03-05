from fastapi import FastAPI
from app.routers import auth, users, accounts, transactions

app = FastAPI(title="Banking API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(accounts.router)
app.include_router(transactions.router)
