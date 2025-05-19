
from pydantic import BaseModel

class SecretCreate(BaseModel):
    name: str
    password: str

class SecretOut(BaseModel):
    id: int
    name: str
    encrypted_password: str

    class Config:
        orm_mode = True
