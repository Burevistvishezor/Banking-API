from pydantic import BaseModel

class AccountCreate(BaseModel):
    user_id: int
