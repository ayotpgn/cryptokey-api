
from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Secret(Base):
    __tablename__ = "secrets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    encrypted_password = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
