from pydantic import BaseModel

class Transfer(BaseModel):
    from_account: int
    to_account: int
    amount: float
