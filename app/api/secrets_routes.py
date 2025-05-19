
from fastapi import APIRouter, Depends
from app.schemas.secret_schema import SecretCreate
from app.core.crypto import encrypt_password, decrypt_password

router = APIRouter()

@router.post("/secrets")
def create_secret(secret: SecretCreate):
    encrypted = encrypt_password(secret.password)
    return {"name": secret.name, "encrypted_password": encrypted}
